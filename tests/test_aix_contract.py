"""Tests for the experimental AIX envelope contract."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


class AixContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "prototypes/aix/aix-message.schema.json").read_text())
        cls.example = json.loads((ROOT / "prototypes/aix/examples/task-request.json").read_text())
        cls.validator = Draft202012Validator(cls.schema, format_checker=Draft202012Validator.FORMAT_CHECKER)

    def test_example_is_valid(self):
        self.assertEqual(list(self.validator.iter_errors(self.example)), [])

    def test_rejects_chain_of_thought_field(self):
        message = json.loads(json.dumps(self.example))
        message["chain_of_thought"] = "private reasoning must not be serialized"
        self.assertTrue(list(self.validator.iter_errors(message)))

    def test_rejects_missing_task_objective(self):
        message = json.loads(json.dumps(self.example))
        del message["task"]["idempotency_key"]
        del message["task"]["objective"]
        self.assertTrue(list(self.validator.iter_errors(message)))

    def test_rejects_invalid_evidence_digest(self):
        message = json.loads(json.dumps(self.example))
        message["evidence_refs"] = [{"evidence_type":"report","uri":"https://example.org/evidence","observed_at":"2026-11-01T20:00:00Z","sha256":"bad"}]
        self.assertTrue(list(self.validator.iter_errors(message)))


if __name__ == "__main__":
    unittest.main()
