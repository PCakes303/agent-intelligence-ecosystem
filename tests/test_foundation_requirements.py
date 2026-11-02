import unittest

from tools.validate_foundation_requirements import validate


def sample():
    return {
        "status": "proposed",
        "requirements": [
            {
                "id": "FND-001", "title": "Authenticate principals",
                "domain": "identity", "priority": "critical",
                "statement": "Every protected operation must identify its principal.",
                "verification": ["contract-test"], "owner": "agent-identity-trust",
                "depends_on": []
            },
            {
                "id": "FND-002", "title": "Authorize operations",
                "domain": "authorization", "priority": "high",
                "statement": "Protected operations must be denied without an allow decision.",
                "verification": ["unit-test"], "owner": "agent-policy-engine",
                "depends_on": ["FND-001"]
            }
        ]
    }


class FoundationRequirementTests(unittest.TestCase):
    def test_valid_requirement_graph(self):
        self.assertEqual(validate(sample()), [])

    def test_duplicate_ids_rejected(self):
        data = sample()
        data["requirements"][1]["id"] = "FND-001"
        self.assertTrue(any("duplicate requirement id" in e for e in validate(data)))

    def test_unknown_dependency_rejected(self):
        data = sample()
        data["requirements"][1]["depends_on"] = ["FND-099"]
        self.assertTrue(any("unknown requirement" in e for e in validate(data)))

    def test_cycle_rejected(self):
        data = sample()
        data["requirements"][0]["depends_on"] = ["FND-002"]
        self.assertTrue(any("cycle detected" in e for e in validate(data)))

    def test_missing_verification_rejected(self):
        data = sample()
        data["requirements"][0]["verification"] = []
        self.assertTrue(any("verification must be a non-empty array" in e for e in validate(data)))


if __name__ == "__main__":
    unittest.main()
