import unittest
from datetime import datetime, timezone
from pathlib import Path
import json
from jsonschema import Draft202012Validator, FormatChecker
from federation_network.trust import PeerRecordError, validate_peer_record

NOW = datetime(2026, 11, 2, 12, 0, tzinfo=timezone.utc)

def record(**changes):
    value = {"peer_id":"peer-west", "network_id":"network-west", "endpoint":"https://west.example.net/federation", "trust_state":"active", "scope":["metadata-read"], "expires_at":"2026-11-03T12:00:00Z", "trust_anchor_sha256":"a"*64, "approval_ref":"change-123", "stop_state":"clear"}
    value.update(changes)
    return value

class PeerTrustTests(unittest.TestCase):
    def test_active_record_requires_review_not_trust(self):
        result=validate_peer_record(record(), now=NOW)
        self.assertEqual(result["status"], "REVIEW_REQUIRED")
        self.assertIn("no peer identity", result["note"])

    def test_pending_peer_is_blocked(self):
        self.assertEqual(validate_peer_record(record(trust_state="pending"), now=NOW)["status"], "BLOCKED")

    def test_revoked_peer_is_blocked(self):
        self.assertEqual(validate_peer_record(record(trust_state="revoked"), now=NOW)["status"], "BLOCKED")

    def test_emergency_stop_blocks_peer(self):
        self.assertEqual(validate_peer_record(record(stop_state="stopped"), now=NOW)["status"], "BLOCKED")

    def test_expired_peer_is_rejected(self):
        with self.assertRaisesRegex(PeerRecordError, "expired"):
            validate_peer_record(record(expires_at="2026-11-01T12:00:00Z"), now=NOW)

    def test_http_and_url_userinfo_are_rejected(self):
        for endpoint in ("http://west.example.net", "https://user:pass@west.example.net/x", "https://west.example.net/x#fragment"):
            with self.subTest(endpoint=endpoint), self.assertRaises(PeerRecordError):
                validate_peer_record(record(endpoint=endpoint), now=NOW)

    def test_duplicate_scope_is_rejected(self):
        with self.assertRaisesRegex(PeerRecordError, "unique"):
            validate_peer_record(record(scope=["metadata-read", "metadata-read"]), now=NOW)

    def test_timezone_naive_expiry_is_rejected(self):
        with self.assertRaisesRegex(PeerRecordError, "timezone"):
            validate_peer_record(record(expires_at="2026-11-03T12:00:00"), now=NOW)

    def test_unknown_fields_are_rejected(self):
        with self.assertRaisesRegex(PeerRecordError, "unknown"):
            validate_peer_record(record(extra="unexpected"), now=NOW)

    def test_expired_now_clock_must_be_aware(self):
        with self.assertRaisesRegex(PeerRecordError, "timezone-aware"):
            validate_peer_record(record(), now=datetime(2026,11,2,12,0))

    def test_state_types_are_rejected_without_type_error(self):
        for field in ("trust_state", "stop_state"):
            with self.subTest(field=field), self.assertRaises(PeerRecordError):
                validate_peer_record(record(**{field: []}), now=NOW)

    def test_schema_accepts_valid_record_and_rejects_http(self):
        schema_path=Path(__file__).resolve().parents[1] / "schemas" / "federation-peer.schema.json"
        schema=json.loads(schema_path.read_text(encoding="utf-8"))
        validator=Draft202012Validator(schema, format_checker=FormatChecker())
        self.assertEqual(list(validator.iter_errors(record())), [])
        self.assertTrue(list(validator.iter_errors(record(endpoint="http://west.example.net"))))

if __name__ == "__main__":
    unittest.main()
