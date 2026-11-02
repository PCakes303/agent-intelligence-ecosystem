# ADR 0005: OSINT collection requires emergency and compliance gates

- Status: accepted
- Date: 2026-11-02
- Scope: osint-collection-framework and future collection adapters

## Context

Public-source metadata does not authorize collection. Network collection creates privacy, legal, access, SSRF, abuse, retention, provenance and operational risks. The ecosystem has approved an independent emergency-control and compliance-governance architecture.

## Decision

The osint-collection-framework contract depends on osint-source-registry, identity-trust, policy-engine, audit-provenance, emergency-control, compliance-governance and secure-supply-chain. No collector may execute unless each dependency's current evidence is verified at request and execution time.

The initial implementation is plan validation only and permits only bounded public non-personal metadata. It prohibits individual targeting, sensitive personal data, credential harvesting, private-record collection, access-control bypass and authenticated access. No network client is included.

## Consequences

- Dependency graph and public catalog must include the safety/compliance edges.
- A valid plan never authorizes execution.
- Future network adapters require a separate architecture decision, SSRF threat model, privacy/legal review and conformance tests.
- Dependencies remain declared until cross-repository integration tests provide reproducible evidence.
