"""Regression tests for registry invariants."""
import json
import unittest
from pathlib import Path

from tools.validate_registry import load_json, validate_registry

ROOT = Path(__file__).resolve().parents[1]


class RegistryValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load_json(ROOT / "schemas/repository-registry.schema.json")
        cls.registry = load_json(ROOT / "registry/repositories.json")
        cls.graph = load_json(ROOT / "registry/dependencies.json")

    def test_committed_registry_is_valid(self):
        self.assertEqual(validate_registry(self.registry, self.schema, self.graph), [])

    def test_rejects_unknown_dependency(self):
        registry = json.loads(json.dumps(self.registry))
        registry["repositories"][0]["dependencies"] = ["does-not-exist"]
        self.assertTrue(any("unknown dependencies" in e for e in validate_registry(registry, self.schema, self.graph)))

    def test_rejects_private_node_in_public_graph(self):
        graph = json.loads(json.dumps(self.graph))
        graph["edges"].append(["master", "private-operations"])
        self.assertTrue(any("private repository leaked" in e for e in validate_registry(self.registry, self.schema, graph)))

    def test_rejects_dependency_cycle(self):
        registry = json.loads(json.dumps(self.registry))
        graph = json.loads(json.dumps(self.graph))
        registry["repositories"][0]["dependencies"] = ["human-guide"]
        graph["edges"].append(["master", "human-guide"])
        self.assertTrue(any("dependency cycle" in e for e in validate_registry(registry, self.schema, graph)))

    def test_rejects_duplicate_repository_id(self):
        registry = json.loads(json.dumps(self.registry))
        registry["repositories"][1]["id"] = registry["repositories"][0]["id"]
        self.assertTrue(any("duplicate repository IDs" in e for e in validate_registry(registry, self.schema, self.graph)))


if __name__ == "__main__":
    unittest.main()
