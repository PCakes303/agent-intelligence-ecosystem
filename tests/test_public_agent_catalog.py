"""Regression tests for public agent catalog consistency."""
import copy
import unittest
from tools.validate_public_agent_catalog import load, validate

class PublicAgentCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from pathlib import Path
        cls.catalog = load(Path("registry/public-agent-catalog.json"))
        cls.registry = load(Path("registry/repositories.json"))
        cls.status = load(Path("registry/implementation-status.json"))
        cls.schema = load(Path("schemas/public-agent-catalog.schema.json"))

    def test_catalog_matches_public_registry(self):
        self.assertEqual(validate(self.catalog, self.registry, self.status, self.schema), [])

    def test_rejects_private_entry(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["repositories"].append(copy.deepcopy(catalog["repositories"][0]))
        catalog["repositories"][-1]["name"] = "agent-ecosystem-private"
        catalog["repositories"][-1]["visibility"] = "private"
        catalog["repository_count"] += 1
        self.assertTrue(validate(catalog, self.registry, self.status, self.schema))

    def test_rejects_stale_dependencies(self):
        catalog = copy.deepcopy(self.catalog)
        catalog["repositories"][0]["dependencies"] = ["invented-dependency"]
        self.assertTrue(any("dependencies drift" in e for e in validate(catalog, self.registry, self.status, self.schema)))

if __name__ == "__main__":
    unittest.main()
