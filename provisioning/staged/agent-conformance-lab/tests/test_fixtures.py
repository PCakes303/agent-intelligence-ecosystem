import unittest
from conformance_lab.fixtures import FixtureError, validate_envelope
from tests.helpers import envelope

class FixtureTests(unittest.TestCase):
    def test_valid_envelope_passes(self):
        self.assertEqual(validate_envelope(envelope())["status"],"PASS")

    def test_unknown_envelope_field_fails(self):
        item=envelope()
        item["payload"]="untrusted"
        with self.assertRaises(FixtureError):
            validate_envelope(item)

    def test_expiry_must_follow_creation(self):
        item=envelope()
        item["expires_at"]=item["created_at"]
        with self.assertRaisesRegex(FixtureError,"expiry"):
            validate_envelope(item)

    def test_expiry_must_fit_ttl(self):
        item=envelope()
        item["expires_at"]="2026-11-02T12:02:00Z"
        with self.assertRaisesRegex(FixtureError,"TTL"):
            validate_envelope(item)

    def test_signature_reference_required(self):
        item=envelope()
        del item["signature_ref"]
        with self.assertRaises(FixtureError):
            validate_envelope(item)

if __name__ == "__main__":
    unittest.main()
