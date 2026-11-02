import unittest

from discovery_network import DiscoveryRecord, RecordValidationError


class DiscoveryRecordTests(unittest.TestCase):
    def record(self, **changes):
        values = dict(
            record_id="rec-1", kind="agent", subject_id="agent:alpha",
            endpoint="https://alpha.example.net/agent", issuer_id="org:example",
            issued_at=100.0, expires_at=200.0, capabilities=("chat",),
            provenance="publisher:node-a", signature="test-signature",
        )
        values.update(changes)
        return DiscoveryRecord(**values)


    def test_rejects_malformed_endpoint(self):
        with self.assertRaises(RecordValidationError):
            self.record(endpoint="https://[::1").validate(now=150, max_lifetime_seconds=200)

    def test_rejects_oversized_record_identifier(self):
        with self.assertRaises(RecordValidationError):
            self.record(record_id="r" * 129).validate(now=150, max_lifetime_seconds=200)

    def test_rejects_boolean_timestamp(self):
        with self.assertRaises(RecordValidationError):
            self.record(issued_at=True).validate(now=150, max_lifetime_seconds=200)

    def test_rejects_excessive_capability_collection(self):
        with self.assertRaises(RecordValidationError):
            self.record(capabilities=tuple(f"cap-{i}" for i in range(129))).validate(now=150, max_lifetime_seconds=200)

    def test_valid_record(self):
        self.record().validate(now=150.0, max_lifetime_seconds=200.0)

    def test_rejects_non_https_endpoint(self):
        with self.assertRaises(RecordValidationError):
            self.record(endpoint="http://alpha.example.net").validate(now=150, max_lifetime_seconds=200)

    def test_rejects_embedded_credentials(self):
        with self.assertRaises(RecordValidationError):
            self.record(endpoint="https://user:pass@alpha.example.net").validate(now=150, max_lifetime_seconds=200)

    def test_rejects_expired_record(self):
        with self.assertRaises(RecordValidationError):
            self.record(expires_at=150).validate(now=150, max_lifetime_seconds=200)

    def test_rejects_excessive_lifetime(self):
        with self.assertRaises(RecordValidationError):
            self.record(expires_at=500).validate(now=150, max_lifetime_seconds=200)

    def test_rejects_missing_signature(self):
        with self.assertRaises(RecordValidationError):
            self.record(signature=" ").validate(now=150, max_lifetime_seconds=200)


if __name__ == "__main__":
    unittest.main()
