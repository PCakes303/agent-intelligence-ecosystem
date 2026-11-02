import json
import unittest

from jsonschema import Draft202012Validator, FormatChecker
from tools.validate_principal import SCHEMA_PATH, validate


VALID = {
    "principal_id": "urn:example:agent:one",
    "principal_type": "agent",
    "issuer": "https://identity.example.test",
    "created_at": "2026-11-01T12:00:00Z",
    "status": "active",
}


class PrincipalValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(cls.schema)
        cls.schema_validator = Draft202012Validator(cls.schema, format_checker=FormatChecker())

    def assert_both_reject(self, document):
        self.assertTrue(validate(document))
        self.assertTrue(list(self.schema_validator.iter_errors(document)))

    def test_valid_principal(self):
        self.assertEqual(validate(VALID), [])
        self.assertEqual(list(self.schema_validator.iter_errors(VALID)), [])

    def test_required_fields_and_unknown_fields(self):
        candidate = dict(VALID)
        del candidate["principal_type"]
        self.assert_both_reject(candidate)
        self.assert_both_reject({**VALID, "unexpected": True})

    def test_principal_id_boundaries(self):
        self.assert_both_reject({**VALID, "principal_id": "ab"})
        self.assert_both_reject({**VALID, "principal_id": "p" * 257})

    def test_principal_type_and_status_enums(self):
        self.assert_both_reject({**VALID, "principal_type": "robot"})
        self.assert_both_reject({**VALID, "status": "trusted"})

    def test_issuer_must_be_absolute_https_or_spiffe_uri(self):
        self.assert_both_reject({**VALID, "issuer": "http://identity.example.test"})
        self.assert_both_reject({**VALID, "issuer": "not-a-uri"})
        self.assert_both_reject({**VALID, "issuer": "https:///missing-host"})

    def test_created_at_must_be_timezone_aware_rfc3339(self):
        self.assert_both_reject({**VALID, "created_at": "2026-11-01T12:00:00"})
        self.assert_both_reject({**VALID, "created_at": "yesterday"})
        self.assert_both_reject({**VALID, "created_at": "2026-11-01T12:00:00+00:00"[:19]})

    def test_optional_field_types_and_lengths(self):
        self.assert_both_reject({**VALID, "display_name": 7})
        self.assert_both_reject({**VALID, "display_name": "n" * 161})
        self.assert_both_reject({**VALID, "public_key_fingerprint": []})
        self.assert_both_reject({**VALID, "public_key_fingerprint": "f" * 257})


if __name__ == "__main__":
    unittest.main()
