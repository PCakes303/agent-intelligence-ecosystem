"""Regression tests for the experimental default-deny policy evaluator."""
import json
import unittest
from pathlib import Path
from tools.policy_engine import validate_and_evaluate

ROOT = Path(__file__).resolve().parents[1]


class PolicyPrototypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.policy = json.loads((ROOT / "prototypes/policy/examples/policy.json").read_text())
        cls.request = json.loads((ROOT / "prototypes/policy/examples/allow-request.json").read_text())
        cls.ps = json.loads((ROOT / "prototypes/policy/policy.schema.json").read_text())
        cls.rs = json.loads((ROOT / "prototypes/policy/request.schema.json").read_text())

    def evaluate(self, policy=None, request=None):
        return validate_and_evaluate(policy or self.policy, request or self.request, self.ps, self.rs)

    def test_matching_allow(self):
        self.assertEqual(self.evaluate()["effect"], "allow")

    def test_unknown_principal_defaults_to_deny(self):
        request = dict(self.request, principal_id="agent://unknown")
        self.assertEqual(self.evaluate(request=request)["decision_id"], "default-deny")

    def test_missing_scope_denies(self):
        request = dict(self.request, scopes=[])
        self.assertEqual(self.evaluate(request=request)["effect"], "deny")

    def test_explicit_deny_overrides_allow(self):
        policy = json.loads(json.dumps(self.policy))
        policy["rules"].append({"id":"deny-source","effect":"deny","principals":["*"],"actions":["source.read"],"resources":["public-source:*"],"required_scopes":[]})
        self.assertEqual(self.evaluate(policy=policy)["decision_id"], "explicit-deny")

    def test_invalid_request_denies(self):
        request = dict(self.request, unexpected="field")
        self.assertEqual(self.evaluate(request=request)["decision_id"], "invalid-input")


if __name__ == "__main__":
    unittest.main()
