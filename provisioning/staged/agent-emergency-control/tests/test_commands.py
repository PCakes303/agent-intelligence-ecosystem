import json
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from emergency_control.commands import CommandError, load_command, validate_command
from tests.helpers import command, approval

class CommandTests(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc)

    def test_valid_stop_command(self):
        parsed = load_command(json.dumps(command(now=self.now)), now=self.now)
        self.assertEqual(parsed.action, "STOP")
        self.assertEqual(parsed.scope.kind, "global")

    def test_resume_requires_two_distinct_approvers(self):
        value = command("RESUME", now=self.now, approvals=[approval("safety-1"), approval("safety-2")])
        self.assertEqual(len(load_command(json.dumps(value), now=self.now).approvals), 2)
        value["approvals"][1]["principal_id"] = "safety-1"
        with self.assertRaises(CommandError):
            load_command(json.dumps(value), now=self.now)

    def test_requester_cannot_approve_own_resume(self):
        value = command("RESUME", now=self.now, approvals=[approval("operator-1"), approval("safety-2")])
        with self.assertRaises(CommandError):
            load_command(json.dumps(value), now=self.now)

    def test_stop_cannot_carry_resume_approvals(self):
        value = command(now=self.now, approvals=[approval("safety-1")])
        with self.assertRaises(CommandError):
            load_command(json.dumps(value), now=self.now)

    def test_expired_command_rejected(self):
        value = command(now=self.now - timedelta(minutes=10))
        with self.assertRaisesRegex(CommandError, "expired"):
            load_command(json.dumps(value), now=self.now)

    def test_command_lifetime_capped_at_five_minutes(self):
        value = command(now=self.now)
        value["expires_at"] = (self.now + timedelta(minutes=6)).isoformat()
        with self.assertRaisesRegex(CommandError, "lifetime"):
            load_command(json.dumps(value), now=self.now)

    def test_naive_timestamp_rejected(self):
        value = command(now=self.now)
        value["issued_at"] = self.now.replace(tzinfo=None).isoformat()
        with self.assertRaises(CommandError):
            load_command(json.dumps(value), now=self.now)

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaisesRegex(CommandError, "duplicate"):
            load_command('{"command_version":"1.0","command_version":"1.0"}', now=self.now)

    def test_nonstandard_numbers_rejected(self):
        with self.assertRaisesRegex(CommandError, "numeric constant"):
            load_command('{"epoch":NaN}', now=self.now)

    def test_byte_and_depth_limits(self):
        with self.assertRaisesRegex(CommandError, "byte limit"):
            load_command(" " * 65_537, now=self.now)
        nested = '{"x":' + ("[" * 17) + "0" + ("]" * 17) + "}"
        with self.assertRaisesRegex(CommandError, "depth limit"):
            load_command(nested, now=self.now)

    def test_future_skew_rejected(self):
        value = command(now=self.now + timedelta(minutes=1))
        with self.assertRaisesRegex(CommandError, "future"):
            load_command(json.dumps(value), now=self.now)

    def test_scope_rules(self):
        value = command(now=self.now, scope={"kind":"global","id":"org-1"})
        with self.assertRaises(CommandError):
            load_command(json.dumps(value), now=self.now)
        value = command(now=self.now, scope={"kind":"agent","id":"*"})
        with self.assertRaises(CommandError):
            load_command(json.dumps(value), now=self.now)

    def test_schema_runtime_parity(self):
        schema_path = Path(__file__).resolve().parents[1] / "schemas" / "emergency-command.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        good = command(now=self.now)
        self.assertEqual(list(validator.iter_errors(good)), [])
        self.assertEqual(load_command(json.dumps(good), now=self.now).action, "STOP")
        bad = command("RESUME", now=self.now, approvals=[approval("safety-1")])
        self.assertTrue(list(validator.iter_errors(bad)))
        with self.assertRaises(CommandError):
            load_command(json.dumps(bad), now=self.now)

if __name__ == "__main__":
    unittest.main()
