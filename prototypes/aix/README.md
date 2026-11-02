# AIX Experimental Envelope

**Status:** experimental research fixture; not a stable protocol and not a production security boundary.

## Purpose

This prototype tests a minimal semantic envelope for task exchange across agent systems. It is deliberately designed to complement existing standards and transports rather than replace them.

## Contract

- Schema: [aix-message.schema.json](aix-message.schema.json)
- Example: [task-request.json](examples/task-request.json)
- Core fields: identity, message type, task intent/objective, idempotency, capability requirements, context/evidence references, security context, and provenance.

## Security properties and limitations

The envelope carries references to authentication and policy context; it does not authenticate a sender or authorize a request by itself. The transport and receiving implementation must verify credentials, trust domain, message integrity, replay controls, scope authorization, and referenced-resource access. Hashes support integrity checks but do not establish truth.

Private model reasoning and chain-of-thought are not part of the contract. Unknown top-level fields are rejected. Extension payloads must be namespaced and governed by a separate compatibility policy.

## Next experiments

1. Map equivalent concepts to MCP and A2A.
2. Add positive and negative conformance fixtures.
3. Measure semantic loss, latency, validation cost, and authorization correctness.
4. Revise the schema only through an ADR and compatibility review.
