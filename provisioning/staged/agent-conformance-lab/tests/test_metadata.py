import unittest
from conformance_lab.metadata import ConformanceError, validate_repository_metadata
from tests.helpers import metadata_documents

class MetadataTests(unittest.TestCase):
    def test_consistent_metadata_passes(self):
        result=validate_repository_metadata(*metadata_documents())
        self.assertEqual(result["status"],"PASS")
        self.assertEqual(result["dependencies"],2)

    def test_repository_identity_mismatch_fails(self):
        manifest,caps,compat=metadata_documents()
        caps["repository_id"]="other"
        with self.assertRaisesRegex(ConformanceError,"identity"):
            validate_repository_metadata(manifest,caps,compat)

    def test_duplicate_manifest_dependencies_fail(self):
        manifest,caps,compat=metadata_documents()
        manifest["dependencies"].append("foundation")
        with self.assertRaisesRegex(ConformanceError,"duplicate"):
            validate_repository_metadata(manifest,caps,compat)

    def test_compatibility_dependency_mismatch_fails(self):
        manifest,caps,compat=metadata_documents()
        compat["dependencies"].pop()
        with self.assertRaisesRegex(ConformanceError,"dependencies differ"):
            validate_repository_metadata(manifest,caps,compat)

    def test_duplicate_capability_ids_fail(self):
        manifest,caps,compat=metadata_documents()
        caps["capabilities"].append({"id":"test.capability"})
        with self.assertRaisesRegex(ConformanceError,"duplicated"):
            validate_repository_metadata(manifest,caps,compat)

    def test_explicit_non_capabilities_required(self):
        manifest,caps,compat=metadata_documents()
        caps["explicit_non_capabilities"]=[]
        with self.assertRaisesRegex(ConformanceError,"non-capabilities"):
            validate_repository_metadata(manifest,caps,compat)

if __name__ == "__main__":
    unittest.main()
