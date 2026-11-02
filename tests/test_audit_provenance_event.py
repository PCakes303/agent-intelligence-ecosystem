import unittest
from tools.validate_audit_event import validate
VALID={"event_id":"evt-1","event_type":"authorization","occurred_at":"2026-11-01T12:00:00Z","actor":{"principal_id":"agent:demo","issuer":"https://issuer.example.test"},"action":"resource.read","target":"resource:demo","outcome":"denied","correlation_id":"corr-1","policy_version":"v1","evidence_refs":[],"data_classification":"public"}
class AuditEventTests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate(VALID),[])
    def test_invalid_timestamp(self): self.assertTrue(validate({**VALID,"occurred_at":"yesterday"}))
    def test_invalid_issuer(self): self.assertTrue(validate({**VALID,"actor":{"principal_id":"agent:demo","issuer":"http://issuer.test"}}))
    def test_invalid_outcome(self): self.assertTrue(validate({**VALID,"outcome":"approved"}))
    def test_evidence_requires_https(self): self.assertTrue(validate({**VALID,"evidence_refs":["file:///secret"]}))
if __name__=="__main__": unittest.main()
