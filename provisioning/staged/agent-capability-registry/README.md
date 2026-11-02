# Agent Capability Registry

Experimental catalog, validation and policy-filtered matching for declared agent capabilities.

## Scope
- Validate bounded, versioned capability declarations.
- Index capabilities in a single-process in-memory registry.
- Match task requirements against declared capability identifiers and attributes.
- Apply a caller-supplied policy decision callback; deny by default when it is absent, raises, or returns false.

The matcher returns candidates, not authorization grants. Capability declarations are assertions, not proof of implementation, quality, safety, availability or identity.

## Quick start
```python
from capability_registry import Capability, CapabilityRegistry, Requirement

registry = CapabilityRegistry(policy_check=lambda agent_id, capability: agent_id == "agent.demo")
registry.register(Capability(
    capability_id="text.summarize",
    agent_id="agent.demo",
    description="Summarizes supplied text",
    version="1.0.0",
    attributes={"domain": "text", "input": "text", "output": "summary"},
))
matches = registry.match([Requirement("text.summarize")])
```

## Contracts
See [capability contract](docs/CAPABILITY-CONTRACT.md) and [threat model](docs/THREAT-MODEL.md). JSON Schema is in `schemas/capability.schema.json`.

## Limitations
No cryptographic attestation, identity issuance, policy engine implementation, distributed index, network API, health checks, benchmark, reputation system or execution scheduler. Policy callbacks must be backed by a trusted policy service before use beyond local experiments.

Python 3.10–3.12 are covered by CI. No package release is published. Repository-specific license selection remains pending review.
