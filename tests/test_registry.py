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

    def test_repository_manifest_template_matches_schema(self):
        manifest_schema = load_json(ROOT / "schemas/repository-manifest.schema.json")
        manifest = load_json(ROOT / "templates/repository/manifest.json")
        errors = list(__import__("jsonschema").Draft202012Validator(manifest_schema).iter_errors(manifest))
        self.assertEqual(errors, [])

    def test_all_staged_component_manifests_match_schema(self):
        manifest_schema = load_json(ROOT / "schemas/repository-manifest.schema.json")
        validator = __import__("jsonschema").Draft202012Validator(manifest_schema)
        paths = sorted((ROOT / "provisioning" / "staged").glob("*/manifest.json"))
        self.assertTrue(paths, "no staged component manifests found")
        errors = []
        for path in paths:
            try:
                manifest = load_json(path)
            except ValueError as exc:
                errors.append(f"{path.relative_to(ROOT)}: {exc}")
                continue
            errors.extend(
                f"{path.relative_to(ROOT)}: {error.message} at {list(error.absolute_path)}"
                for error in validator.iter_errors(manifest)
            )
        self.assertEqual(errors, [])

    def test_staged_component_inventory_matches_public_registry(self):
        expected = {
            item["name"]
            for item in self.registry["repositories"]
            if item["visibility"] == "public" and item["name"] != "agent-intelligence-ecosystem"
        }
        staged_root = ROOT / "provisioning" / "staged"
        actual = {path.name for path in staged_root.iterdir() if path.is_dir()}
        self.assertEqual(actual, expected)

    def test_staged_manifest_dependencies_match_registry(self):
        by_id = {item["id"]: item for item in self.registry["repositories"]}
        paths = sorted((ROOT / "provisioning" / "staged").glob("*/manifest.json"))
        self.assertEqual(len(paths), len(by_id) - 2)  # exclude master and private operations
        errors = []
        for path in paths:
            manifest = load_json(path)
            row = by_id.get(manifest.get("id"))
            if row is None:
                errors.append(f"{path}: unknown registry id {manifest.get('id')}")
                continue
            manifest_deps = {item["id"] for item in manifest.get("dependencies", [])}
            registry_deps = set(row.get("dependencies", []))
            if manifest_deps != registry_deps:
                errors.append(
                    f"{path}: manifest dependencies {sorted(manifest_deps)} "
                    f"do not match registry dependencies {sorted(registry_deps)}"
                )
        self.assertEqual(errors, [])

    def test_capability_and_compatibility_metadata_match_manifest(self):
        paths = sorted((ROOT / "provisioning" / "staged").glob("*/manifest.json"))
        errors = []
        for path in paths:
            manifest = load_json(path)
            capabilities = load_json(path.parent / "capabilities.json")
            compatibility = load_json(path.parent / "compatibility.json")
            if capabilities.get("repository") != manifest.get("name"):
                errors.append(f"{path.parent}: capability repository name mismatch")
            if capabilities.get("repository_id") != manifest.get("id"):
                errors.append(f"{path.parent}: capability repository ID mismatch")
            if compatibility.get("repository") != manifest.get("name"):
                errors.append(f"{path.parent}: compatibility repository name mismatch")
            registry_ids = {item["id"] for item in self.registry["repositories"]}
            compatibility_deps = {
                item["repository_id"] for item in compatibility.get("dependencies", [])
            }
            if not compatibility_deps.issubset(registry_ids):
                errors.append(f"{path.parent}: compatibility references unknown registry IDs")
        self.assertEqual(errors, [])

    def test_readme_license_status_matches_manifest(self):
        paths = sorted((ROOT / "provisioning" / "staged").glob("*/manifest.json"))
        errors = []
        for path in paths:
            manifest = load_json(path)
            if manifest.get("license", {}).get("status") == "pending-review":
                readme = (path.parent / "README.md").read_text(encoding="utf-8")
                if "pending-review" not in readme:
                    errors.append(f"{path.parent}: README omits pending license review status")
                if "applies a scoped mixed-license policy" in readme:
                    errors.append(f"{path.parent}: README implies file-level licensing is already applied")
        self.assertEqual(errors, [])

    def test_no_public_repositories_remain_uncreated(self):
        status = load_json(ROOT / "registry" / "implementation-status.json")
        self.assertEqual(status["observed"]["public_repositories_missing"], 0)
        self.assertEqual(status["staged_not_created"], [])

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
