# ADR 0008: Conformance reports require pinned evidence and explicit blocked states

- Status: accepted
- Date: 2026-11-02
- Scope: agent-conformance-lab

## Context

Local schema validation does not demonstrate runtime interoperability, production security or legal compliance. Declared dependencies are not tested integrations.

## Decision

The conformance lab validates local repository metadata and synthetic protocol fixtures, and builds deterministic reports with PASS, FAIL and BLOCKED states. Missing integration evidence remains BLOCKED. The lab does not execute arbitrary repository code, connect to live agents, benchmark production swarms or certify security/compliance.

Identity, policy, audit, emergency-control, compliance-governance and secure-supply-chain evidence are mandatory security gates.

## Consequences

- Registry dependency graph and public catalog include the required gates.
- No dependency moves to tested status without pinned reproducible integration fixtures.
- Report digests provide integrity checks only; reports are not signed attestations.
