# ADR 0007: Entity resolution is public-entity candidate generation only

- Status: accepted
- Date: 2026-11-02
- Scope: osint-entity-resolution

## Context

Entity correlation can become personal identity resolution or profiling. The knowledge graph consumes upstream entity records but does not itself perform resolution.

## Decision

The initial entity-resolution contract is limited to public organizations, software projects, datasets, publications and public registries. It emits deterministic review-required candidates based on public identifiers, aliases and name similarity. Scores are heuristic, not probabilities. It does not match people, infer sensitive attributes, auto-merge records or write to the knowledge graph.

The repository depends on evidence, schema registry, identity, policy, audit, emergency-control, compliance-governance and secure-supply-chain contracts. A human reviewer must accept any candidate through a separate authenticated and auditable workflow.

## Consequences

- Dependency graph and public catalog include the safety and compliance edges.
- Person matching and private-individual profiling remain explicitly unsupported.
- Knowledge-graph integration requires a versioned adapter and reproducible fixtures.
- Dependencies remain declared until integration tests prove interoperability.
