import unittest
from capability_registry import Capability, Requirement, ValidationError


class ModelTests(unittest.TestCase):
    def test_valid_model(self):
        Capability('text.summarize', 'agent.one', 'Summarizes text', '1.2.3', {'domain': 'text'}).validate()

    def test_invalid_version(self):
        with self.assertRaises(ValidationError):
            Capability('text.summarize', 'agent.one', 'Summarizes text', 'v1', {}).validate()

    def test_bad_identifier(self):
        with self.assertRaises(ValidationError):
            Capability('bad id', 'agent.one', 'Description', '1.0.0', {}).validate()

    def test_requirement(self):
        Requirement('text.summarize', {'domain': 'text'}).validate()


if __name__ == '__main__':
    unittest.main()
