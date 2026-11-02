"""Identity, audit schema, and tamper-evidence regression tests."""
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
from tools.audit_chain import append_event, verify_chain

ROOT = Path(__file__).resolve().parents[1]


class IdentityAuditTests(unittest.TestCase):
    def test_identity_example_valid_and_unknown_material_rejected(self):
        schema = json.loads((ROOT / "schemas/principal-identity.schema.json").read_text())
        example = json.loads((ROOT / "examples/principal-identity.example.json").read_text())
        validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
        self.assertEqual(list(validator.iter_errors(example)), [])
        example["credential_material"] = "must-not-be-stored"
        self.assertTrue(list(validator.iter_errors(example)))

    def test_audit_example_valid(self):
        schema = json.loads((ROOT / "schemas/audit-event.schema.json").read_text())
        example = json.loads((ROOT / "examples/audit-event.example.json").read_text())
        validator = Draft202012Validator(schema, format_checker=Draft202012Validator.FORMAT_CHECKER)
        self.assertEqual(list(validator.iter_errors(example)), [])

    def test_hash_chain_verifies_and_detects_tampering(self):
        first = append_event([], {"event_id":"1","action":"read","outcome":"success"})
        second = append_event([first], {"event_id":"2","action":"write","outcome":"denied"})
        self.assertEqual(verify_chain([first, second]), (True, "chain valid"))
        altered = dict(second, outcome="success")
        self.assertFalse(verify_chain([first, altered])[0])

    def test_hash_chain_detects_reordering(self):
        first = append_event([], {"event_id":"1","action":"read"})
        second = append_event([first], {"event_id":"2","action":"write"})
        self.assertFalse(verify_chain([second, first])[0])


if __name__ == "__main__":
    unittest.main()
