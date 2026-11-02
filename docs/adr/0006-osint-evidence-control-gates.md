# ADR 0006: OSINT evidence requires emergency and compliance gates

- Status: accepted
- Date: 2026-11-02
- Scope: osint-evidence-engine and future evidence ingestion/export adapters

## Context

Evidence records may contain sensitive material and can be relied on for operational, legal or security decisions. Integrity, retention, privacy and provenance must not be treated as optional metadata.

## Decision

The osint-evidence-engine contract depends on osint-collection, audit-provenance, secure-supply-chain, emergency-control and compliance-governance. Ingestion and export adapters must verify source/collection authority, identity, policy, emergency state, privacy/compliance review and audit evidence.

The initial implementation is limited to public non-personal manifests, SHA-256 content verification and deterministic hash-linked event metadata. It does not store payloads, sign records, provide trusted timestamps or manage legal holds.

## Consequences

- Dependency graph and public catalog include the emergency-control and compliance-governance edges.
- No legal chain-of-custody claim is made.
- Future private storage and ingestion adapters require a separate threat model, retention/legal-hold design and independent security review.
