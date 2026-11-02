import unittest

from discovery_network import DiscoveryRecord, DiscoveryRegistry


class DiscoveryRegistryTests(unittest.TestCase):
    def setUp(self):
        self.now = [100.0]
        self.registry = DiscoveryRegistry(
            verifier=lambda record: record.signature == "valid",
            trust_evaluator=lambda issuer: issuer == "org:trusted",
            clock=lambda: self.now[0],
            max_lifetime_seconds=100,
            max_records=2,
        )

    def record(self, record_id="rec-1", **changes):
        values = dict(
            record_id=record_id, kind="agent", subject_id="agent:alpha",
            endpoint="https://alpha.example.net/agent", issuer_id="org:trusted",
            issued_at=90.0, expires_at=150.0, capabilities=("chat", "planning"),
            provenance="publisher:node-a", signature="valid",
        )
        values.update(changes)
        return DiscoveryRecord(**values)


    def test_truthy_non_boolean_verifier_result_is_rejected(self):
        registry = DiscoveryRegistry(
            verifier=lambda record: "true",
            trust_evaluator=lambda issuer: True,
            clock=lambda: self.now[0],
        )
        with self.assertRaises(PermissionError):
            registry.publish(self.record())

    def test_truthy_non_boolean_trust_result_is_rejected(self):
        registry = DiscoveryRegistry(
            verifier=lambda record: True,
            trust_evaluator=lambda issuer: "trusted",
            clock=lambda: self.now[0],
        )
        with self.assertRaises(PermissionError):
            registry.publish(self.record())

    def test_nonfinite_clock_fails_closed(self):
        registry = DiscoveryRegistry(
            verifier=lambda record: True,
            trust_evaluator=lambda issuer: True,
            clock=lambda: float("nan"),
        )
        with self.assertRaises(RuntimeError):
            registry.publish(self.record())

    def test_nonfinite_lifetime_config_is_rejected(self):
        with self.assertRaises(ValueError):
            DiscoveryRegistry(
                verifier=lambda record: True,
                trust_evaluator=lambda issuer: True,
                max_lifetime_seconds=float("inf"),
            )

    def test_noninteger_capacity_config_is_rejected(self):
        with self.assertRaises(ValueError):
            DiscoveryRegistry(
                verifier=lambda record: True,
                trust_evaluator=lambda issuer: True,
                max_records=1.5,
            )

    def test_publish_and_query(self):
        self.registry.publish(self.record())
        self.assertEqual(len(self.registry.query(kind="agent", capability="chat")), 1)

    def test_untrusted_issuer_is_rejected(self):
        with self.assertRaises(PermissionError):
            self.registry.publish(self.record(issuer_id="org:unknown"))

    def test_invalid_signature_is_rejected(self):
        with self.assertRaises(PermissionError):
            self.registry.publish(self.record(signature="invalid"))

    def test_missing_callbacks_fail_closed(self):
        registry = DiscoveryRegistry(verifier=None, trust_evaluator=None, clock=lambda: self.now[0])
        with self.assertRaises(PermissionError):
            registry.publish(self.record())

    def test_expired_record_is_not_returned(self):
        self.registry.publish(self.record())
        self.now[0] = 151.0
        self.assertEqual(self.registry.query(), [])

    def test_trust_revocation_hides_existing_record(self):
        trusted = [True]
        registry = DiscoveryRegistry(
            verifier=lambda record: True,
            trust_evaluator=lambda issuer: trusted[0],
            clock=lambda: self.now[0],
        )
        registry.publish(self.record())
        trusted[0] = False
        self.assertEqual(registry.query(), [])

    def test_duplicate_record_id_is_rejected(self):
        self.registry.publish(self.record())
        with self.assertRaises(ValueError):
            self.registry.publish(self.record())

    def test_capacity_is_bounded(self):
        self.registry.publish(self.record("rec-1"))
        self.registry.publish(self.record("rec-2"))
        with self.assertRaises(OverflowError):
            self.registry.publish(self.record("rec-3"))

    def test_query_filters(self):
        self.registry.publish(self.record())
        self.registry.publish(self.record("rec-2", kind="service", capabilities=("search",)))
        self.assertEqual(len(self.registry.query(kind="service")), 1)
        self.assertEqual(len(self.registry.query(capability="search")), 1)


if __name__ == "__main__":
    unittest.main()
