import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_log import AuditError, append_event, read_records, verify_records

def event(event_id="evt-1"):
    return {
        "event_id": event_id,
        "timestamp": "2026-01-01T00:00:00Z",
        "event_type": "policy.decision",
        "actor": {"id": "agent:test", "type": "agent"},
        "action": "read",
        "resource": "dataset:demo",
        "outcome": "success",
        "details": {"decision": "allow"}
    }

class AuditLogTests(unittest.TestCase):
    def test_append_and_verify_single_event(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            append_event(path, event())
            self.assertEqual(verify_records(read_records(path)), 1)

    def test_chain_links_multiple_events(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            first = append_event(path, event("one"))
            second = append_event(path, event("two"))
            self.assertEqual(second["previous_hash"], first["event_hash"])
            self.assertEqual(verify_records(read_records(path)), 2)

    def test_modified_payload_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            append_event(path, event())
            records = read_records(path)
            records[0]["action"] = "delete"
            with self.assertRaisesRegex(AuditError, "event_hash mismatch"):
                verify_records(records)

    def test_broken_link_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            append_event(path, event("one"))
            append_event(path, event("two"))
            records = read_records(path)
            records[1]["previous_hash"] = "0" * 64
            records[1]["event_hash"] = __import__("tools.audit_log", fromlist=["digest_event"]).digest_event(records[1])
            with self.assertRaisesRegex(AuditError, "previous_hash"):
                verify_records(records)

    def test_missing_field_rejected(self):
        with self.assertRaisesRegex(AuditError, "missing required"):
            from tools.audit_log import validate_event
            validate_event({"event_id": "incomplete"})

    def test_bad_outcome_rejected(self):
        from tools.audit_log import validate_event
        bad = event()
        bad["outcome"] = "maybe"
        with self.assertRaisesRegex(AuditError, "outcome"):
            validate_event(bad)

    def test_caller_cannot_supply_digest_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = event()
            bad["event_hash"] = "0" * 64
            with self.assertRaisesRegex(AuditError, "must not provide"):
                append_event(Path(tmp) / "events.jsonl", bad)

    def test_blank_line_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            path.write_text("\n", encoding="utf-8")
            with self.assertRaisesRegex(AuditError, "blank lines"):
                read_records(path)

if __name__ == "__main__":
    unittest.main()
