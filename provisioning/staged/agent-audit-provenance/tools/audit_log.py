#!/usr/bin/env python3
"""Append and verify an experimental SHA-256 hash-chained JSONL audit log."""
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

HEX64 = re.compile(r"^[a-f0-9]{64}$")
OUTCOMES = {"success", "failure", "denied", "unknown"}
REQUIRED = {"event_id", "timestamp", "event_type", "actor", "action", "resource", "outcome", "details"}
ALLOWED = REQUIRED | {"previous_hash", "event_hash"}

class AuditError(ValueError):
    pass

def canonical_bytes(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def digest_event(event):
    payload = {k: v for k, v in event.items() if k != "event_hash"}
    return hashlib.sha256(canonical_bytes(payload)).hexdigest()

def validate_event(event, require_hash=False):
    if not isinstance(event, dict):
        raise AuditError("event must be a JSON object")
    missing = REQUIRED - event.keys()
    unknown = event.keys() - ALLOWED
    if unknown:
        raise AuditError("unknown fields: " + ", ".join(sorted(unknown)))
    if missing:
        raise AuditError("missing required fields: " + ", ".join(sorted(missing)))
    if not all(isinstance(event[k], str) and event[k].strip() for k in ("event_id", "timestamp", "event_type", "action", "resource")):
        raise AuditError("event identifiers, timestamp, type, action, and resource must be non-empty strings")
    try:
        parsed_timestamp = datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
        if parsed_timestamp.tzinfo is None:
            raise ValueError("timezone offset required")
    except ValueError as exc:
        raise AuditError("timestamp must be RFC 3339 / ISO-8601") from exc
    actor = event["actor"]
    if not isinstance(actor, dict) or not isinstance(actor.get("id"), str) or not actor["id"].strip() or not isinstance(actor.get("type"), str) or not actor["type"].strip():
        raise AuditError("actor must contain non-empty id and type strings")
    if event["outcome"] not in OUTCOMES:
        raise AuditError("outcome must be success, failure, denied, or unknown")
    if not isinstance(event["details"], dict):
        raise AuditError("details must be an object")
    if require_hash:
        if event.get("previous_hash") is not None and not (isinstance(event.get("previous_hash"), str) and HEX64.fullmatch(event["previous_hash"])):
            raise AuditError("previous_hash must be null or a lowercase SHA-256 digest")
        if not isinstance(event.get("event_hash"), str) or not HEX64.fullmatch(event["event_hash"]):
            raise AuditError("event_hash must be a lowercase SHA-256 digest")

def append_event(log_path, raw_event):
    if not isinstance(raw_event, dict):
        raise AuditError("event input must be a JSON object")
    if "event_hash" in raw_event or "previous_hash" in raw_event:
        raise AuditError("append input must not provide previous_hash or event_hash")
    validate_event(raw_event)
    path = Path(log_path)
    previous = None
    if path.exists() and path.stat().st_size:
        records = read_records(path)
        verify_records(records)
        previous = records[-1]["event_hash"]
    event = dict(raw_event)
    event["previous_hash"] = previous
    event["event_hash"] = digest_event(event)
    validate_event(event, require_hash=True)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(event, sort_keys=True, ensure_ascii=False) + "\n")
    return event

def read_records(path):
    records = []
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            for number, line in enumerate(handle, 1):
                if not line.strip():
                    raise AuditError(f"line {number}: blank lines are not allowed")
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise AuditError(f"line {number}: invalid JSON: {exc.msg}") from exc
    except OSError as exc:
        raise AuditError(f"cannot read log: {exc}") from exc
    return records

def verify_records(records):
    previous = None
    for number, event in enumerate(records, 1):
        try:
            validate_event(event, require_hash=True)
            if event["previous_hash"] != previous:
                raise AuditError("previous_hash does not match prior event")
            expected = digest_event(event)
            if event["event_hash"] != expected:
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
            raw = json.loads(Path(args.event).read_text(encoding="utf-8"))
            event = append_event(args.log, raw)
            print(json.dumps({"status": "appended", "event_id": event["event_id"], "event_hash": event["event_hash"]}, sort_keys=True))
        else:
            count = verify_records(read_records(args.log))
            print(json.dumps({"status": "valid", "events_verified": count}, sort_keys=True))
        return 0
    except (AuditError, OSError, json.JSONDecodeError) as exc:
        print(f"audit-log error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
