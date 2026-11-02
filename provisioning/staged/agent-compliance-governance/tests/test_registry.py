import json
import tempfile
import unittest
from pathlib import Path
from compliance_governance.registry import RegistryError, load_json, validate_documents, validate_repository
from tests.helpers import ROOT, documents

class RegistryTests(unittest.TestCase):
    def test_repository_registers_validate(self):
        result = validate_repository(ROOT)
        self.assertEqual(result["status"], "valid")
        self.assertEqual(result["legal_records"], 6)
        self.assertEqual(result["controls"], 11)
        self.assertEqual(result["evidence_records"], 0)
        self.assertFalse(result["legal_applicability_determined"])
        self.assertFalse(result["compliance_certification"])

    def test_duplicate_legal_record_id_rejected(self):
        legal, controls, evidence = documents()
        legal["records"].append(dict(legal["records"][0]))
        with self.assertRaisesRegex(RegistryError, "duplicate legal record"):
            validate_documents(legal, controls, evidence, ROOT / "schemas")

    def test_unknown_legal_record_reference_rejected(self):
        legal, controls, evidence = documents()
        controls["controls"][0]["linked_legal_records"].append("not-a-real-law")
        with self.assertRaisesRegex(RegistryError, "unknown legal records"):
            validate_documents(legal, controls, evidence, ROOT / "schemas")

    def test_unknown_evidence_control_reference_rejected(self):
        legal, controls, evidence = documents()
        evidence["records"].append({
            "evidence_id":"synthetic-evidence-1","control_ids":["NO-999"],"system_id":"synthetic-system",
            "artifact_type":"test_result","description":"Synthetic fixture for invalid reference testing",
            "collected_at":"2026-11-02T12:00:00Z","source_uri":"https://example.invalid/evidence",
            "sha256":"a"*64,"retention_policy":"test-only","access_class":"internal",
            "integrity_status":"pending","reviewer":None
        })
        with self.assertRaisesRegex(RegistryError, "unknown controls"):
            validate_documents(legal, controls, evidence, ROOT / "schemas")

    def test_invalid_legal_status_rejected(self):
        legal, controls, evidence = documents()
        legal["records"][0]["status"] = "compliant"
        with self.assertRaisesRegex(RegistryError, "schema error"):
            validate_documents(legal, controls, evidence, ROOT / "schemas")

    def test_next_review_must_not_precede_last_verified(self):
        legal, controls, evidence = documents()
        legal["records"][0]["next_review"] = "2026-10-01"
        with self.assertRaisesRegex(RegistryError, "next_review before"):
            validate_documents(legal, controls, evidence, ROOT / "schemas")

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "duplicate.json"
            path.write_text('{"a":1,"a":2}', encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "duplicate JSON key"):
                load_json(path)

    def test_nonstandard_json_number_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nan.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "non-standard"):
                load_json(path)

    def test_document_byte_and_depth_limits(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "large.json"
            path.write_text(" " * (2_097_153), encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "byte limit"):
                load_json(path)
            path.write_text('{"x":' + ("[" * 33) + "0" + ("]" * 33) + "}", encoding="utf-8")
            with self.assertRaisesRegex(RegistryError, "nesting limit"):
                load_json(path)

    def test_empty_evidence_index_is_valid_and_not_a_compliance_claim(self):
        legal, controls, evidence = documents()
        result = validate_documents(legal, controls, evidence, ROOT / "schemas")
        self.assertEqual(result["evidence_records"], 0)
        self.assertFalse(result["compliance_certification"])

if __name__ == "__main__":
    unittest.main()
