import json
import tempfile
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

from tools.audit_log import AuditError, append_event, read_records, verify_records, validate_event, load_event_file

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas" / "audit-event.schema.json").read_text(encoding="utf-8"))
Draft202012Validator.check_schema(SCHEMA)
SCHEMA_VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())


def event(event_id="evt-1"):
    return {
        "event_id": event_id, "timestamp": "2026-01-01T00:00:00Z",
        "event_type": "policy.decision", "actor": {"id": "agent:test", "type": "agent"},
        "action": "read", "resource": "dataset:demo", "outcome": "success",
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
            records = read_records(path); records[0]["action"] = "delete"
            with self.assertRaisesRegex(AuditError, "event_hash mismatch"):
                verify_records(records)

    def test_broken_link_is_detected(self):
        from tools.audit_log import digest_event
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            append_event(path, event("one")); append_event(path, event("two"))
            records = read_records(path); records[1]["previous_hash"] = "0" * 64
            records[1]["event_hash"] = digest_event(records[1])
            with self.assertRaisesRegex(AuditError, "previous_hash"):
                verify_records(records)

    def test_missing_unknown_and_bad_outcome_rejected(self):
        with self.assertRaisesRegex(AuditError, "missing required"):
            validate_event({"event_id": "incomplete"})
        bad = event(); bad["unmodeled"] = True
        with self.assertRaisesRegex(AuditError, "unknown fields"):
            validate_event(bad)
        bad = event(); bad["outcome"] = "maybe"
        with self.assertRaises(AuditError):
            validate_event(bad)

    def test_caller_cannot_supply_digest_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = event(); bad["event_hash"] = "0" * 64
            with self.assertRaisesRegex(AuditError, "must not provide"):
                append_event(Path(tmp) / "events.jsonl", bad)

    def test_timezone_required(self):
        bad = event(); bad["timestamp"] = "2026-01-01T00:00:00"
        with self.assertRaises(AuditError):
            validate_event(bad)

    def test_schema_parity_and_field_bounds(self):
        raw = event(); raw["previous_hash"] = None; raw["event_hash"] = "0" * 64
        self.assertEqual(list(SCHEMA_VALIDATOR.iter_errors(raw)), [])
        for bad in (
            {**raw, "event_id": "e" * 129},
            {**raw, "event_type": "t" * 129},
            {**raw, "action": "a" * 257},
            {**raw, "resource": "r" * 1025},
            {**raw, "actor": {"id": "i" * 129, "type": "agent"}},
        ):
            with self.assertRaises(AuditError):
                validate_event({k:v for k,v in bad.items() if k not in {"previous_hash","event_hash"}})
            self.assertTrue(list(SCHEMA_VALIDATOR.iter_errors(bad)))

    def test_details_budgets(self):
        bad = event(); bad["details"] = {f"k{i}": "v" for i in range(65)}
        with self.assertRaisesRegex(AuditError, "property limit"):
            validate_event(bad)
        bad = event(); bad["details"] = {"large": "x" * 5000}
        with self.assertRaises(AuditError):
            validate_event(bad)
        bad = event()
        nested = 1
        for key in reversed("abcdefghijklmnop"):
            nested = {key: nested}
        bad["details"] = {"deep": nested}
        with self.assertRaisesRegex(AuditError, "nesting"):
            validate_event(bad)

    def test_duplicate_json_keys_nonfinite_depth_and_blank_lines_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            for raw in ('{"event_id":"x","event_id":"y"}', '{"x":NaN}', '{"x":' + ("[" * 33) + "0" + ("]" * 33) + '}'):
                path.write_text(raw + "\n", encoding="utf-8")
                with self.assertRaises(AuditError):
                    read_records(path)
            path.write_text("\n", encoding="utf-8")
            with self.assertRaisesRegex(AuditError, "blank lines"):
                read_records(path)

    def test_event_file_parser_limits(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "event.json"
            path.write_text('{"x":1,"x":2}', encoding="utf-8")
            with self.assertRaisesRegex(AuditError, "duplicate"):
                load_event_file(path)
            path.write_bytes(b"x" * (1_048_577))
            with self.assertRaisesRegex(AuditError, "byte limit"):
                load_event_file(path)

    def test_log_and_event_byte_limits(self):
        from tools import audit_log
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "events.jsonl"
            from unittest.mock import patch
            with patch.object(audit_log, "MAX_LOG_BYTES", 8):
                path.write_bytes(b"x" * 9)
                with self.assertRaisesRegex(AuditError, "byte limit"):
                    read_records(path)
            path.write_bytes(b"")
            with patch.object(audit_log, "MAX_EVENT_BYTES", 64):
                bad = event(); bad["details"] = {"blob": "x" * 100}
                with self.assertRaises(AuditError):
                    append_event(path, bad)


if __name__ == "__main__":
    unittest.main()
