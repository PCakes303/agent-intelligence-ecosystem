#!/usr/bin/env python3
"""Bounded experimental SHA-256 hash-chained JSONL audit log; not authenticated or tamper-proof storage."""
import argparse
import hashlib
import json
import math
import sys
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "audit-event.schema.json"
HEX64 = __import__("re").compile(r"^[a-f0-9]{64}$")
OUTCOMES = {"success", "failure", "denied", "unknown"}
REQUIRED = {"event_id", "timestamp", "event_type", "actor", "action", "resource", "outcome", "details"}
ALLOWED = REQUIRED | {"previous_hash", "event_hash"}
MAX_EVENT_BYTES = 1_048_576
MAX_LOG_BYTES = 67_108_864
MAX_EVENTS = 100_000
MAX_JSON_DEPTH = 32
MAX_DETAILS_BYTES = 65_536


class AuditError(ValueError):
    pass


def canonical_bytes(value):
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError, OverflowError) as exc:
        raise AuditError("event contains a non-JSON or non-finite value") from exc


def digest_event(event):
    payload = {key: value for key, value in event.items() if key != "event_hash"}
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()


def _pairs_no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise AuditError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _check_json_depth(raw):
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
                raise AuditError("JSON nesting exceeds depth limit")
        elif char in "]}":
            depth -= 1
            if depth < 0:
                raise AuditError("invalid JSON structure")


def _validate_details(value, depth=0):
    if depth > 16:
        raise AuditError("details nesting exceeds depth limit")
    if isinstance(value, str):
        if len(value) > 4096:
            raise AuditError("details string exceeds length limit")
    elif isinstance(value, list):
        if len(value) > 256:
            raise AuditError("details array exceeds item limit")
        for item in value:
            _validate_details(item, depth + 1)
    elif isinstance(value, dict):
        if len(value) > 64:
            raise AuditError("details object exceeds property limit")
        for key, item in value.items():
            if not isinstance(key, str) or not key or len(key) > 128:
                raise AuditError("details keys must be non-empty strings of at most 128 characters")
            _validate_details(item, depth + 1)
    elif isinstance(value, float) and not math.isfinite(value):
        raise AuditError("details cannot contain non-finite numbers")
    elif value is not None and not isinstance(value, (bool, int, float)):
        raise AuditError("details contain an unsupported JSON value")


def _schema_validate(event):
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(event),
            key=lambda error: (tuple(str(part) for part in error.absolute_path), error.message),
        )
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        raise AuditError(f"normative audit schema unavailable or invalid: {type(exc).__name__}") from exc
    if errors:
        error = errors[0]
        location = ".".join(str(part) for part in error.absolute_path) or "<root>"
        raise AuditError(f"schema violation at {location}: {error.message}")


def validate_event(event, require_hash=False):
    if not isinstance(event, dict):
        raise AuditError("event must be a JSON object")
    missing = REQUIRED - event.keys()
    unknown = event.keys() - ALLOWED
    if unknown:
        raise AuditError("unknown fields: " + ", ".join(sorted(unknown)))
    if missing:
        raise AuditError("missing required fields: " + ", ".join(sorted(missing)))
    if not isinstance(event.get("actor"), dict):
        raise AuditError("actor must be an object")
    if not isinstance(event.get("details"), dict):
        raise AuditError("details must be an object")
    _validate_details(event["details"])
    if len(canonical_bytes(event["details"])) > MAX_DETAILS_BYTES:
        raise AuditError("details exceed serialized byte limit")
    candidate = dict(event)
    if not require_hash:
        candidate["previous_hash"] = None
        candidate["event_hash"] = "0" * 64
    _schema_validate(candidate)
    try:
        parsed = datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
    except (ValueError, AttributeError) as exc:
        raise AuditError("timestamp must be RFC 3339 / ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise AuditError("timestamp must include a timezone offset")
    if event["outcome"] not in OUTCOMES:
        raise AuditError("outcome must be success, failure, denied, or unknown")
    if require_hash:
        previous = event.get("previous_hash")
        if previous is not None and not (isinstance(previous, str) and HEX64.fullmatch(previous)):
            raise AuditError("previous_hash must be null or a lowercase SHA-256 digest")
        if not isinstance(event.get("event_hash"), str) or not HEX64.fullmatch(event["event_hash"]):
            raise AuditError("event_hash must be a lowercase SHA-256 digest")


def load_event_file(path):
    raw_bytes = Path(path).read_bytes()
    if len(raw_bytes) > MAX_EVENT_BYTES:
        raise AuditError("event input exceeds byte limit")
    try:
        raw = raw_bytes.decode("utf-8")
        _check_json_depth(raw)
        return json.loads(raw, object_pairs_hook=_pairs_no_duplicates,
                          parse_constant=lambda value: (_ for _ in ()).throw(AuditError(f"invalid JSON number: {value}")))
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        raise AuditError("event input is invalid UTF-8 or JSON") from exc


def append_event(log_path, raw_event):
    if not isinstance(raw_event, dict):
        raise AuditError("event input must be a JSON object")
    if "event_hash" in raw_event or "previous_hash" in raw_event:
        raise AuditError("append input must not provide previous_hash or event_hash")
    validate_event(raw_event)
    path = Path(log_path)
    previous = None
    if path.exists() and path.stat().st_size:
        if path.stat().st_size > MAX_LOG_BYTES:
            raise AuditError("audit log exceeds byte limit")
        records = read_records(path)
        verify_records(records)
        previous = records[-1]["event_hash"]
    if path.exists() and path.stat().st_size >= MAX_LOG_BYTES:
        raise AuditError("audit log exceeds byte limit")
    if path.exists() and path.stat().st_size and len(records) >= MAX_EVENTS:
        raise AuditError("audit log exceeds event count limit")
    event = dict(raw_event)
    event["previous_hash"] = previous
    event["event_hash"] = digest_event(event)
    validate_event(event, require_hash=True)
    line = json.dumps(event, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n"
    encoded_length = len(line.encode("utf-8"))
    if encoded_length > MAX_EVENT_BYTES:
        raise AuditError("serialized event exceeds byte limit")
    if path.exists() and path.stat().st_size + encoded_length > MAX_LOG_BYTES:
        raise AuditError("audit log exceeds byte limit")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    return event


def read_records(path):
    records = []
    log_path = Path(path)
    try:
        if log_path.stat().st_size > MAX_LOG_BYTES:
            raise AuditError("audit log exceeds byte limit")
        with log_path.open("r", encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if number > MAX_EVENTS:
                    raise AuditError("audit log exceeds event count limit")
                if not line.strip():
                    raise AuditError(f"line {number}: blank lines are not allowed")
                if len(line.encode("utf-8")) > MAX_EVENT_BYTES:
                    raise AuditError(f"line {number}: event exceeds byte limit")
                _check_json_depth(line)
                try:
                    records.append(json.loads(line, object_pairs_hook=_pairs_no_duplicates,
                                              parse_constant=lambda value: (_ for _ in ()).throw(AuditError(f"invalid JSON number: {value}"))))
                except (json.JSONDecodeError, RecursionError) as exc:
                    raise AuditError(f"line {number}: invalid JSON") from exc
    except (OSError, UnicodeDecodeError) as exc:
        raise AuditError(f"cannot read log: {exc}") from exc
    return records


def verify_records(records):
    previous = None
    for number, event in enumerate(records, 1):
        try:
            validate_event(event, require_hash=True)
            if event["previous_hash"] != previous:
                raise AuditError("previous_hash does not match prior event")
            if event["event_hash"] != digest_event(event):
                raise AuditError("event_hash mismatch")
        except AuditError as exc:
            raise AuditError(f"line {number}: {exc}") from exc
        previous = event["event_hash"]
    return len(records)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    add = sub.add_parser("append", help="append an event JSON object")
    add.add_argument("--log", required=True)
    add.add_argument("--event", required=True)
    verify = sub.add_parser("verify", help="verify all records in a JSONL log")
    verify.add_argument("--log", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "append":
            raw = load_event_file(args.event)
            event = append_event(args.log, raw)
            print(json.dumps({"status": "appended", "event_id": event["event_id"], "event_hash": event["event_hash"]}, sort_keys=True))
        else:
            count = verify_records(read_records(args.log))
            print(json.dumps({"status": "valid", "events_verified": count}, sort_keys=True))
        return 0
    except (AuditError, OSError, UnicodeDecodeError, json.JSONDecodeError, RecursionError) as exc:
        print(f"audit-log error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
