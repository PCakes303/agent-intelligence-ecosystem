"""Tamper-evident hash-chain helpers for audit event fixtures.

A valid hash chain detects changes relative to the chain being checked. It does
not prove that an event is true, complete, authorized, or honestly originated.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

GENESIS = None


def canonical_bytes(value: dict[str, Any]) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def append_event(events: list[dict[str, Any]], event: dict[str, Any]) -> dict[str, Any]:
    record = dict(event)
    record.pop("event_hash", None)
    record["previous_hash"] = events[-1]["event_hash"] if events else GENESIS
    record["event_hash"] = hashlib.sha256(canonical_bytes(record)).hexdigest()
    return record


def verify_chain(events: list[dict[str, Any]]) -> tuple[bool, str]:
    previous = GENESIS
    for index, event in enumerate(events):
        supplied = event.get("event_hash")
        if event.get("previous_hash") != previous:
            return False, f"event {index}: previous_hash mismatch"
        payload = dict(event)
        payload.pop("event_hash", None)
        expected = hashlib.sha256(canonical_bytes(payload)).hexdigest()
        if supplied != expected:
            return False, f"event {index}: event_hash mismatch"
        previous = supplied
    return True, "chain valid"
