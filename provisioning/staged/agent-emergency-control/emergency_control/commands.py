"""Strict, bounded emergency-command parser. No cryptographic verification is performed."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, FormatChecker

MAX_COMMAND_BYTES = 65_536
MAX_JSON_DEPTH = 16
MAX_COMMAND_LIFETIME = timedelta(minutes=5)
MAX_FUTURE_SKEW = timedelta(seconds=30)
_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "emergency-command.schema.json"
_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())
_UUID = re.compile(r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$")

class CommandError(ValueError):
    """Raised for malformed, stale, expired or structurally unsafe commands."""

def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise CommandError(f"duplicate JSON key: {key}")
        result[key] = value
    return result

def _reject_constant(value: str) -> None:
    raise CommandError(f"non-standard JSON numeric constant: {value}")

def _check_raw_bounds(raw: str) -> None:
    if not isinstance(raw, str):
        raise CommandError("command input must be text")
    try:
        size = len(raw.encode("utf-8"))
    except UnicodeError as exc:
        raise CommandError("command input is not valid UTF-8 text") from exc
    if size > MAX_COMMAND_BYTES:
        raise CommandError("command exceeds byte limit")
    depth = 0
    in_string = False
    escaped = False
    for char in raw:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                raise CommandError("command JSON nesting exceeds depth limit")
        elif char in "]}":
            depth -= 1
            if depth < 0:
                raise CommandError("invalid JSON structure")

def _parse_time(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise CommandError("invalid RFC3339 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise CommandError("timestamp must include a timezone")
    return parsed.astimezone(timezone.utc)

@dataclass(frozen=True)
class Scope:
    kind: str
    id: str

@dataclass(frozen=True)
class Approval:
    principal_id: str
    key_id: str
    signature: str

@dataclass(frozen=True)
class EmergencyCommand:
    command_id: str
    epoch: int
    action: str
    scope: Scope
    issued_at: datetime
    expires_at: datetime
    actor_principal_id: str
    actor_key_id: str
    actor_signature: str
    reason: str
    approvals: tuple[Approval, ...]

def validate_command(value: Any, *, now: datetime) -> EmergencyCommand:
    if not isinstance(value, dict):
        raise CommandError("command must be an object")
    if now.tzinfo is None or now.utcoffset() is None:
        raise CommandError("now must be timezone-aware")
    errors = sorted(_VALIDATOR.iter_errors(value), key=lambda e: (list(e.absolute_path), e.message))
    if errors:
        first = errors[0]
        path = ".".join(str(part) for part in first.absolute_path)
        raise CommandError(f"schema validation failed at {path or '<root>'}: {first.message}")
    command_id = value["command_id"]
    if not _UUID.fullmatch(command_id):
        raise CommandError("command_id must be a canonical UUID")
    scope = value["scope"]
    if scope["kind"] == "global" and scope["id"] != "*":
        raise CommandError("global scope id must be '*'")
    if scope["kind"] != "global" and scope["id"] == "*":
        raise CommandError("non-global scope cannot use wildcard id")
    actor_id = value["actor"]["principal_id"]
    approvals = tuple(Approval(**item) for item in value["approvals"])
    approval_ids = [item.principal_id for item in approvals]
    if len(set(approval_ids)) != len(approval_ids):
        raise CommandError("resume approvers must be distinct")
    if actor_id in approval_ids:
        raise CommandError("requester cannot count as a resume approver")
    issued_at = _parse_time(value["issued_at"])
    expires_at = _parse_time(value["expires_at"])
    current = now.astimezone(timezone.utc)
    if issued_at > current + MAX_FUTURE_SKEW:
        raise CommandError("command issued_at is too far in the future")
    if expires_at <= current:
        raise CommandError("command has expired")
    if expires_at <= issued_at or expires_at - issued_at > MAX_COMMAND_LIFETIME:
        raise CommandError("command lifetime must be positive and no longer than five minutes")
    return EmergencyCommand(
        command_id=command_id,
        epoch=value["epoch"],
        action=value["action"],
        scope=Scope(**scope),
        issued_at=issued_at,
        expires_at=expires_at,
        actor_principal_id=actor_id,
        actor_key_id=value["actor"]["key_id"],
        actor_signature=value["actor"]["signature"],
        reason=value["reason"],
        approvals=approvals,
    )

def load_command(raw: str, *, now: datetime) -> EmergencyCommand:
    _check_raw_bounds(raw)
    try:
        value = json.loads(raw, object_pairs_hook=_pairs, parse_constant=_reject_constant)
    except CommandError:
        raise
    except (json.JSONDecodeError, UnicodeError, RecursionError, TypeError, ValueError) as exc:
        raise CommandError("invalid command JSON") from exc
    return validate_command(value, now=now)
