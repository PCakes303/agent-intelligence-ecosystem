# Executable Implementation Plan

This plan defines deliverables and acceptance gates. It does not imply that future work is already implemented.

## Batch 1 — Master control plane (implemented)
- [x] Publish 30-entry registry and dependency graph.
- [x] Publish architecture, governance, security, roadmap, and synchronization design.
- [x] Add executable registry validation and regression tests.
- [x] Add repository manifest schema and reusable repository starter template.
- [x] Pin CI actions to immutable commit SHAs.
- [x] Add public-only scaffold generator and explicit-confirmation GitHub CLI provisioner.
- [x] Add machine-readable list of 28 missing public repositories.
- Acceptance verified: CI validates schema, registry/graph consistency, unique IDs/names, counts, private boundary, acyclic dependencies, manifest template, resource manifest example, policy smoke test, and regression tests. Latest verified run before the current workflow update passed 25 tests; a new run is pending for the latest additions.

## Batch 2 — Foundation repository specifications (01–07)
- [x] Add machine-readable initial requirements for all seven foundation/security repositories.
- [x] Add resource manifest schema, example, CLI validator, and negative tests.
- [x] Add principal identity schema and example.
- [x] Add audit event schema, example, hash-chain utility, and tamper tests.
- [x] Add default-deny policy schemas, reference evaluator, CLI, and precedence tests.
- [ ] Add schema-registry compatibility runner and schema publication index.
- [ ] Add identity issuance/rotation/revocation state machine and authenticated integration demo.
- [ ] Add SBOM/provenance/signature release workflow.
- [ ] Transfer prototypes into their owning standalone repositories after provisioning.
No repository advances beyond research/scaffolding solely on prose.

## Batch 3 — AIX and transport prototypes (08–10)
Implement JSON schemas, reference encoder/decoder, MCP/A2A mapping fixtures, validation tests, and authorization-negative cases. Measure translation fidelity and latency.

## Batch 4 — Swarm vertical slice (11–15)
Implement a minimal end-to-end task delegation flow across two independently authenticated nodes. Include idempotency, replay rejection, bounded retry, node failure, and state reconciliation tests.

## Batch 5 — OSINT evidence vertical slice (16–20)
Use a permitted public test source or synthetic fixture. Preserve source, retrieval time, transformation log, content hash, uncertainty, and reproducible processing. Include privacy and policy-denial tests.

## Batch 6 — Adoption and federation (21–25)
Implement sandboxed adapter execution, skill manifest validation, conformance runner, and two-domain federation prototype with explicit trust and authorization.

## Portfolio-wide acceptance gates
- Requirements trace to tests.
- CI runs on pull requests and default-branch pushes.
- Dependencies are versioned and vulnerability-scanned.
- No secrets are committed.
- Interfaces have compatibility tests.
- Releases have SBOM/provenance appropriate to maturity.
- Security boundaries and failure behavior are tested.
- Public/private data-flow checks are negative-tested.

## Progress reporting
Every batch report lists concrete commits, tests run and outcomes, artifacts produced, verified behavior, known gaps, and the next acceptance gate.
