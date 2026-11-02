import unittest
from capability_registry import Capability, CapabilityRegistry, Requirement


class RegistryTests(unittest.TestCase):

    def test_registered_attributes_are_snapshotted(self):
        attributes = {'domain': 'text'}
        registry = CapabilityRegistry(decision_callback=lambda agent, item: True)
        registry.register(Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', attributes))
        attributes['domain'] = 'admin'
        result = registry.match([Requirement('text.summarize', {'domain': 'text'})])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].attributes['domain'], 'text')

    def test_returned_attributes_are_immutable(self):
        registry = CapabilityRegistry(decision_callback=lambda agent, item: True)
        registry.register(Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {'domain': 'text'}))
        result = registry.match([Requirement('text.summarize')])
        with self.assertRaises(TypeError):
            result[0].attributes['domain'] = 'admin'

    def test_requirement_count_is_bounded(self):
        registry = CapabilityRegistry(decision_callback=lambda agent, item: True, max_requirements=2)
        requirements = (Requirement('text.summarize') for _ in range(3))
        with self.assertRaises(ValueError):
            registry.match(requirements)

    def test_truthy_non_boolean_policy_result_is_denied(self):
        registry = CapabilityRegistry(decision_callback=lambda agent, item: 'allow')
        registry.register(Capability('text.summarize', 'agent.one', 'Summarizes text', '1.0.0', {}))
        self.assertEqual(registry.match([Requirement('text.summarize')]), [])

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
