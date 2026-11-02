# Repository 17 staging status

Experimental single-process coordination scaffold prepared in master staging. Includes validated task declarations, deterministic candidate selection, policy-gated idempotent submission, dispatch and acknowledgement binding, bounded retry attempts, lease-expiry recovery, completion/failure transitions, optional audit events, AIX mapping guidance, JSON Schema, tests and Python 3.10–3.12 CI.

The initial vertical slice is a coordinator library with injected candidate resolver and dispatch adapter. It is not a network service, distributed scheduler or consensus protocol. State and idempotency records are in-memory and volatile. No cryptographic caller authentication, durable state, cross-replica replay protection, distributed locking, federation, consensus, production AIX codec integration or production adapters are implemented.

Dependencies on Swarm Runtime, AIX Core, Agent Discovery Network and Agent Capability Registry remain `declared`, not `tested`.

Next: deploy and test the scaffold; then build authenticated transport integration, durable task state, cross-repository AIX/discovery/capability fixtures and multi-node recovery tests.
