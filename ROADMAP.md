# Roadmap

## Phase 0 — Control plane and architecture
- [x] Approve the 30-repository portfolio and core architectural decisions.
- [x] Provision the public master and private operations repositories.
- [x] Complete registry schema and automated registry validation.
- [x] Publish initial ADRs, contribution/security governance, and repository template.
- [ ] Implement reviewed cross-repository synchronization in the integration repository (repository not yet provisioned).
- [x] Define public/private information-flow controls and reconciliation design.
- [x] Add a tested public-only scaffold generator and GitHub CLI provisioning script.

## Phase 1 — Foundation and cybersecurity (repositories 01–07)
Initial master-repository prototypes now include resource-manifest, principal-identity, and audit-event schemas; a resource-manifest validator; a default-deny policy evaluator; an audit hash-chain utility; and executable regression fixtures. The seven standalone repositories are not yet provisioned. Exit requires these contracts and implementations to be transferred into their owning repositories, completed threat models, signed identity lifecycle demonstrations, policy enforcement integration, supply-chain attestations, and cross-repository tests.

## Phase 2 — Protocols (08–10)
AIX semantic specification, codecs, and transport gateway. Exit requires interoperability prototypes and measured translation fidelity, latency, validation cost, and authorization correctness.

## Phase 3 — Swarm infrastructure (11–15)
Discovery, capabilities, runtime, coordination, and state mesh. Exit requires failure-injection tests, idempotent task semantics, bounded retries, and documented consistency guarantees.

## Phase 4 — OSINT and intelligence (16–20)
Source registry, authorized collection, evidence, entity resolution, and knowledge graph. Exit requires source-use controls, provenance, uncertainty reporting, and evaluation datasets with appropriate rights.

## Phase 5 — Adoption and expansion (21–25)
Tool adapters, skills, sandboxing, conformance lab, and federation. Exit requires security tests, reproducible conformance suites, and independently operated federation demonstrations.

## Continuous cross-cutting work
The AI-native discovery and human-facing guide repositories evolve alongside the technical phases. The integration repository provides contract validation and change-impact automation. The private repository holds restricted internal material under separate access controls.

A phase is not complete merely because documentation or repository scaffolding exists. Each milestone report must state what was researched, designed, implemented, tested, published, verified, known limitations, risks, affected dependencies, and next milestone.
