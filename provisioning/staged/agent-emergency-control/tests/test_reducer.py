import unittest
from datetime import datetime, timezone
from emergency_control.commands import validate_command
from emergency_control.reducer import StopState, VerificationEvidence, TransitionError, apply_command
from tests.helpers import command, approval

class Verifier:
    def __init__(self, evidence=None, error=False):
        self.evidence = evidence or VerificationEvidence(True, True, True, True, True, True)
        self.error = error
    def verify(self, command):
        if self.error:
            raise RuntimeError("synthetic verifier outage")
        return self.evidence

class ReducerTests(unittest.TestCase):
    def parse(self, action="STOP", epoch=1, approvals=None):
        now = datetime.now(timezone.utc)
        return validate_command(command(action, epoch, now, approvals=approvals), now=now)

    def test_stop_activates_even_when_resume_policy_is_false(self):
        evidence = VerificationEvidence(True, True, True, True, False, False)
        state = apply_command(StopState(), self.parse(), Verifier(evidence))
        self.assertTrue(state.active)
        self.assertEqual(state.epoch, 1)

    def test_resume_requires_active_matching_scope_and_two_person_evidence(self):
        stop = apply_command(StopState(), self.parse("STOP", 1), Verifier())
        resume = self.parse("RESUME", 2, [approval("safety-1"), approval("safety-2")])
        with self.assertRaisesRegex(TransitionError, "resume-quorum"):
            apply_command(stop, resume, Verifier(VerificationEvidence(True, True, True, True, False, True)))
        resumed = apply_command(stop, resume, Verifier())
        self.assertFalse(resumed.active)
        self.assertEqual(resumed.epoch, 2)

    def test_replay_and_non_monotonic_epoch_rejected(self):
        stop = apply_command(StopState(), self.parse("STOP", 2), Verifier())
        with self.assertRaisesRegex(TransitionError, "epoch"):
            apply_command(stop, self.parse("STOP", 2), Verifier())

    def test_missing_or_non_boolean_verification_denies(self):
        for evidence in (VerificationEvidence(), VerificationEvidence(signature_valid=1, actor_authorized=True, revocation_clear=True, command_fresh=True)):
            with self.assertRaises(TransitionError):
                apply_command(StopState(), self.parse(), Verifier(evidence))

    def test_verifier_failure_fails_closed(self):
        with self.assertRaisesRegex(TransitionError, "verification-error"):
            apply_command(StopState(), self.parse(), Verifier(error=True))

    def test_resume_policy_must_allow(self):
        stop = apply_command(StopState(), self.parse("STOP", 1), Verifier())
        resume = self.parse("RESUME", 2, [approval("safety-1"), approval("safety-2")])
        evidence = VerificationEvidence(True, True, True, True, True, False)
        with self.assertRaisesRegex(TransitionError, "resume-policy"):
            apply_command(stop, resume, Verifier(evidence))

    def test_cannot_resume_without_active_stop(self):
        resume = self.parse("RESUME", 2, [approval("safety-1"), approval("safety-2")])
        with self.assertRaisesRegex(TransitionError, "no-matching"):
            apply_command(StopState(), resume, Verifier())

    def test_active_scope_cannot_be_overwritten(self):
        stop = apply_command(StopState(), self.parse("STOP", 1), Verifier())
        now = datetime.now(timezone.utc)
        other = validate_command(command("STOP", 2, now, scope={"kind":"agent","id":"agent-9"}), now=now)
        with self.assertRaisesRegex(TransitionError, "scope-conflict"):
            apply_command(stop, other, Verifier())

if __name__ == "__main__":
    unittest.main()
