# Executable Implementation Plan

This plan defines deliverables and acceptance gates. It does not imply that future work is already implemented.

## Batch 1 — Master control plane (implemented)
- [x] Publish 30-entry registry and dependency graph.
- [x] Publish architecture, governance, security, roadmap, and synchronization design.
- [x] Add executable registry validation and regression tests.
- [x] Add repository manifest schema and reusable repository starter template.
- [x] Pin CI actions to immutable commit SHAs.
- [x] Add public-only scaffold generator and explicit-confirmation GitHub CLI provisioner.
- [x] Add machine-readable list of 21 missing public repositories.
- Acceptance verified: CI validates schema, registry/graph consistency, unique IDs/names, counts, private boundary, acyclic dependencies, manifest template, resource manifest example, policy evaluator smoke test, and regression tests. Latest verified run: success, 25 tests passed, including AIX, policy, identity, audit-chain, scaffold-generation, and registry regressions.

## Batch 2 — Foundation repository specifications (01–10)
- [x] Add machine-readable initial requirements for all seven foundation/security repositories.
- [x] Add resource manifest schema, example, CLI validator, and negative tests.
- [x] Add principal identity schema and example.
- [x] Add audit event schema, example, hash-chain utility, and tamper tests.
- [x] Add default-deny policy schemas, reference evaluator, CLI, and precedence tests.
- [ ] Add schema-registry compatibility runner and schema publication index.
- [ ] Add identity issuance/rotation/revocation state machine and authenticated integration demo.
- [x] Add initial supply-chain artifact record schema, illustrative fixture, validator, tests, SBOM policy, provenance/attestation guidance, and release-verification procedure in the master repository.  
- [x] Add audit-provenance event schema, fixture, standard-library validator, negative tests, and Starter → Developer → Production contract.  
- [x] Publish policy-engine contract and starter learning path; retain default-deny reference evaluator and regression tests.  
- [x] Add reusable Starter build, Makefile, tests, and pinned read-only CI workflow to the public repository scaffold template.  
- [ ] Add SBOM generation, cryptographic provenance/signature verification, and release workflow.
- [ ] Transfer policy, audit, and supply-chain contracts into their owning standalone repositories after provisioning.
No repository advances beyond research/scaffolding solely on prose.

Package readiness audit: the master has a pinned development dependency but no distribution build metadata or verified release artifact. The seven existing public project repositories reviewed are specification/schema/tooling repositories with no root-level language package build manifests. Do not publish packages until reusable libraries or executables exist and reproducible build, license, SBOM, provenance, and install tests are in place.

## Batch 3 — AIX and transport prototypes (08–10)
- [x] Add AIX Core experimental envelope contract, task lifecycle semantics, example validation CLI, and regression tests.
- [ ] Add reference encoder/decoder and deterministic canonical JSON codec.
- [ ] Add MCP/A2A mapping fixtures and measure semantic translation fidelity.
- [ ] Add transport adapter, authentication/authorization-negative cases, replay controls, and latency measurements.
AIX remains an extension layer over established standards, not a replacement protocol.

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
