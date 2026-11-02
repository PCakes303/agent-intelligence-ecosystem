import unittest
from conformance_lab.metadata import ConformanceError
from conformance_lab.reports import build_report, validate_report
from tests.helpers import COMMIT, NOW, check

class ReportTests(unittest.TestCase):
    def make(self, checks):
        return build_report(suite_id="synthetic-suite",subject_repository="PCakes303/test-repo",subject_commit=COMMIT,generated_at=NOW,checks=checks,limitations=["Local fixture tests only; no live interoperability."])

    def test_all_pass_yields_pass(self):
        report=self.make([check("metadata.consistency")])
        self.assertEqual(report["overall_status"],"PASS")
        self.assertTrue(validate_report(report))

    def test_any_failure_yields_fail(self):
        report=self.make([check("metadata.consistency"),check("security.gate","FAIL")])
        self.assertEqual(report["overall_status"],"FAIL")

    def test_blocked_gate_yields_blocked(self):
        report=self.make([check("metadata.consistency"),check("identity.integration","BLOCKED")])
        self.assertEqual(report["overall_status"],"BLOCKED")

    def test_empty_checks_yield_blocked_not_pass(self):
        report=self.make([])
        self.assertEqual(report["overall_status"],"BLOCKED")
        self.assertEqual(report["checks"][0]["status"],"BLOCKED")

    def test_report_digest_detects_tampering(self):
        report=self.make([check("metadata.consistency")])
        report["checks"][0]["description"]="tampered"
        with self.assertRaisesRegex(ConformanceError,"digest mismatch"):
            validate_report(report)

    def test_overall_status_must_match_checks(self):
        report=self.make([check("security.gate","BLOCKED")])
        report["overall_status"]="PASS"
        with self.assertRaisesRegex(ConformanceError,"overall_status"):
            validate_report(report)

    def test_report_is_deterministic_for_same_inputs(self):
        first=self.make([check("metadata.consistency")])
        second=self.make([check("metadata.consistency")])
        self.assertEqual(first,second)

if __name__ == "__main__":
    unittest.main()
