import unittest
from capability_registry import Capability, CapabilityRegistry, Requirement


class RegistryTests(unittest.TestCase):
    def test_registration_and_query(self):
        registry = CapabilityRegistry(decision_callback=lambda agent, item: True)
        item = Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {'domain': 'text'})
        registry.register(item)
        self.assertEqual(registry.match([Requirement('text.summarize')]), [item])

    def test_no_callback_returns_no_candidates(self):
        registry = CapabilityRegistry(decision_callback=None)
        item = Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {})
        registry.register(item)
        self.assertEqual(registry.match([Requirement('text.summarize')]), [])


if __name__ == '__main__':
    unittest.main()
