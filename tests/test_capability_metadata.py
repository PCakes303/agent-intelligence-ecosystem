import unittest
from tools.validate_capability_metadata import validate_capabilities, validate_compatibility

class MetadataTests(unittest.TestCase):
    def test_capability_claim_requires_evidence(self):
        data={"capabilities_version":"1.1.0","repository":"demo-repo","repository_id":"demo","maturity":"scaffolding",
              "capabilities":[{"id":"demo.a","name":"Demo","status":"implemented","description":"A real feature","evidence":[]}],
              "explicit_non_capabilities":[]}
        self.assertTrue(any("needs evidence" in e for e in validate_capabilities(data)))
    def test_compatibility_test_requires_evidence(self):
        data={"compatibility_version":"1.1.0","repository":"demo-repo","policy":"Declared dependencies are not proof of interoperability.",
              "dependencies":[{"repository_id":"base","version_range":"*","status":"tested","evidence":[]}],
              "tested_combinations":[],"breaking_change_policy":"Major versions mark breaking contract changes and migrations."}
        self.assertTrue(any("tested claim needs evidence" in e for e in validate_compatibility(data)))
    def test_declared_dependency_is_valid(self):
        data={"compatibility_version":"1.1.0","repository":"demo-repo","policy":"Declared dependencies are not proof of interoperability.",
              "dependencies":[{"repository_id":"base","version_range":"*","status":"declared","evidence":[]}],
              "tested_combinations":[],"breaking_change_policy":"Major versions mark breaking contract changes and migrations."}
        self.assertEqual(validate_compatibility(data),[])
if __name__=="__main__": unittest.main()
