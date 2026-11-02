import unittest
from capability_registry import Capability, CapabilityRegistry, Requirement


class RegistryTests(unittest.TestCase):
    def test_registration_and_query(self):
        registry = CapabilityRegistry(decision_callback=lambda agent, item: True)
        item = Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {'domain': 'text'})
        registry.register(item)
        self.assertEqual(registry.match([Requirement('text.summarize')]), [item])

    def test_all_requirements_must_be_met_by_same_agent(self):
        registry = CapabilityRegistry(decision_callback=lambda agent, item: True)
        registry.register(Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {}))
        registry.register(Capability('image.detect', 'agent.one', 'Detects images', '1.0.0', {}))
        registry.register(Capability('text.summarize', 'agent.two', 'Summarizes text', '1.0.0', {}))
        result = registry.match([Requirement('text.summarize'), Requirement('image.detect')])
        self.assertEqual([(x.agent_id, x.capability_id) for x in result],
                         [('agent.one', 'image.detect'), ('agent.one', 'text.summarize')])

    def test_no_callback_returns_no_candidates(self):
        registry = CapabilityRegistry(decision_callback=None)
        item = Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {})
        registry.register(item)
        self.assertEqual(registry.match([Requirement('text.summarize')]), [])


if __name__ == '__main__':
    unittest.main()
