"""Fail-closed local peer declaration validation only."""
from __future__ import annotations
from datetime import datetime, timezone
import re
from typing import Any, Mapping
from urllib.parse import urlsplit

class PeerRecordError(ValueError):
    pass

_ID = re.compile(r"^[a-z0-9][a-z0-9-]{1,62}$")
_DIGEST = re.compile(r"^[a-f0-9]{64}$")

def _timestamp(value: Any) -> datetime:
    if not isinstance(value, str) or len(value) > 64:
        raise PeerRecordError("expires_at must be a bounded timezone-aware timestamp")
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise PeerRecordError("expires_at must be a valid ISO timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise PeerRecordError("expires_at must include a timezone")
    return parsed

def validate_peer_record(record: Mapping[str, Any], *, now: datetime | None = None) -> dict[str, Any]:
    if not isinstance(record, Mapping):
        raise PeerRecordError("peer record must be an object")
    required = {"peer_id", "network_id", "endpoint", "trust_state", "scope", "expires_at", "trust_anchor_sha256", "approval_ref", "stop_state"}
    if set(record) != required:
        raise PeerRecordError("peer record has missing or unknown fields")
    for field in ("peer_id", "network_id"):
        value = record[field]
        if not isinstance(value, str) or not _ID.fullmatch(value):
            raise PeerRecordError(f"{field} has invalid format")
    endpoint = record["endpoint"]
    if not isinstance(endpoint, str) or len(endpoint) > 512:
        raise PeerRecordError("endpoint must be a bounded HTTPS URL")
    parsed = urlsplit(endpoint)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.fragment:
        raise PeerRecordError("endpoint must be HTTPS without userinfo or fragment")
    if not isinstance(record["scope"], list) or not record["scope"] or len(record["scope"]) > 32:
        raise PeerRecordError("scope must contain 1 to 32 entries")
    if any(not isinstance(item, str) or not _ID.fullmatch(item) for item in record["scope"]):
        raise PeerRecordError("scope entries must be bounded identifiers")
    if len(set(record["scope"])) != len(record["scope"]):
        raise PeerRecordError("scope entries must be unique")
    if record["trust_state"] not in {"pending", "active", "revoked"}:
        raise PeerRecordError("trust_state is invalid")
    if record["stop_state"] not in {"clear", "stopped"}:
        raise PeerRecordError("stop_state is invalid")
    if not isinstance(record["trust_anchor_sha256"], str) or not _DIGEST.fullmatch(record["trust_anchor_sha256"]):
        raise PeerRecordError("trust anchor digest must be lowercase SHA-256 hex")
    if not isinstance(record["approval_ref"], str) or not record["approval_ref"] or len(record["approval_ref"]) > 256:
        raise PeerRecordError("approval_ref must be a bounded non-empty reference")
    expires = _timestamp(record["expires_at"])
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None or current.utcoffset() is None:
        raise PeerRecordError("now must be timezone-aware")
    if expires <= current:
        raise PeerRecordError("peer trust declaration is expired")
    status = "BLOCKED" if record["trust_state"] != "active" or record["stop_state"] != "clear" else "REVIEW_REQUIRED"
    return {"status": status, "peer_id": record["peer_id"], "scope": list(record["scope"]), "note": "Local declaration validation only; no peer identity or signature was verified."}
