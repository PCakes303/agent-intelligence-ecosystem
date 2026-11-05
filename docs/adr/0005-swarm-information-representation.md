# ADR 0005 — Swarm-native information representation research expansion

- **Status:** Accepted
- **Date:** 2026-11-05
- **Decision owners:** MrCakes931 / PCakes303
- **Scope:** Research and implementation boundary for adaptive compression and swarm-native information representation

## Context

The existing ecosystem includes AIX codecs, distributed swarm state, runtime coordination, provenance, and knowledge-graph components. A separate research effort is exploring whether distributed systems can reduce the total cost of making information useful through shared structure, adaptive representations, selective reconstruction, and computation over encoded data.

The research must not be confused with a claim that arbitrary data can be compressed beyond information-theoretic limits. It must also not create a competing AIX or swarm runtime.

## Decision

Create two connected but independently scoped repositories:

1. **Private:** [swarm-information-research](https://github.com/PCakes303/swarm-information-research) — authoritative private record for hypotheses, taxonomy, theory, experiments, negative results, benchmark protocol, and research decisions.
2. **Public:** [adaptive-swarm-compression](https://github.com/PCakes303/adaptive-swarm-compression) — independently buildable experimental implementation for codecs, representation capsules, pipeline composition, benchmarks, and later collective/selective operations.

The private repository is excluded from public discovery exports and all automatic public synchronization. The public repository must never require access to private notes.

## Integration boundaries

- Reuse aix-codecs for compatible codec abstractions where appropriate.
- Reuse aix-core for representation negotiation semantics where appropriate.
- Reuse agent-resource-manifest and agent-schema-registry for portable resource metadata and schema governance.
- Reuse swarm-state-mesh and swarm-runtime for future distributed state and execution integration.
- Reuse intelligence-knowledge-graph for graph-specific representation experiments.
- Reuse agent-audit-provenance for transformation lineage and evidence records.

These are declared integration relationships, not claims of tested interoperability.

## Non-negotiable constraints

- Distinguish exact, bounded-loss, approximate, and semantic representations.
- Preserve authoritative source identity and provenance.
- Include dictionaries, indexes, models, metadata, transfer, coordination, verification, and recovery in cost accounting.
- Never claim arbitrary lossless compression to an arbitrarily small fixed size.
- Treat shared representations as potential privacy and trust-boundary risks.
- Do not claim distributed swarm behavior until implemented and tested.

## Consequences

The master registry and public catalog include the new public implementation. The private research repository is listed only in the restricted registry with public_export false. The coordinated inventory now contains 34 repositories: 32 public and 2 private.

The new public project is experimental. It requires its own CI, benchmarks, compatibility review, and security hardening before wider integration.
