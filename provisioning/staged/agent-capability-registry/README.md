# Agent Capability Registry

Experimental catalog and matching layer for declared agent capabilities.

Use `Capability`, `Requirement`, and `CapabilityRegistry` from the `capability_registry` package. The registry is process-local and bounded; it snapshots and freezes registered attribute mappings and caps each match request at 128 requirements by default. Matching is advisory; it does not authenticate agents, grant permissions, execute work, or prove that a declaration is true.

Quick start:

```python
from capability_registry import Capability, CapabilityRegistry, Requirement
registry = CapabilityRegistry(decision_callback=lambda agent, item: True)
registry.register(Capability('text.summarize', 'agent.demo', 'Summarizes text', '1.0.0', {}))
print(registry.match([Requirement('text.summarize')]))
```

See `docs/CAPABILITY-CONTRACT.md`, `docs/THREAT-MODEL.md`, and `schemas/capability.schema.json`. Python 3.10–3.12 CI is configured. No release is published and the license decision is pending review.
