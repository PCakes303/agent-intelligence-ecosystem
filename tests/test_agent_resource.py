"""Tests for the public agent resource manifest contract."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


class AgentResourceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads((ROOT / "schemas/agent-resource.schema.json").read_text())
        cls.example = json.loads((ROOT / "examples/agent-resource.example.json").read_text())
        cls.validator = Draft202012Validator(cls.schema, format_checker=Draft202012Validator.FORMAT_CHECKER)

    def test_example_is_valid(self):
        self.assertEqual(list(self.validator.iter_errors(self.example)), [])

    def test_rejects_embedded_secret_field(self):
        value = json.loads(json.dumps(self.example))
        value["api_key"] = "not-a-real-secret"
        self.assertTrue(list(self.validator.iter_errors(value)))

    def test_rejects_missing_trust_domain(self):
        value = json.loads(json.dumps(self.example))
        del value["security"]["trust_domain"]
        self.assertTrue(list(self.validator.iter_errors(value)))

    def test_rejects_unknown_capability_field(self):
        value = json.loads(json.dumps(self.example))
        value["capabilities"][0]["shell_command"] = "unsafe"
        self.assertTrue(list(self.validator.iter_errors(value)))


if __name__ == "__main__":
    unittest.main()
