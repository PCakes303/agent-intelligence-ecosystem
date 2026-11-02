# Executable Implementation Plan

This plan defines deliverables and acceptance gates. It does not imply that future work is already implemented.

## Batch 1 — Master control plane (current)
- [x] Publish 30-entry registry and dependency graph.
- [x] Publish architecture, governance, security, roadmap, and synchronization design.
- [ ] Make registry validation executable and regression-tested.
- [ ] Add manifest schema and reusable repository starter template.
- [ ] Pin CI actions to immutable commit SHAs.
- Acceptance: CI validates schema, exact registry/graph consistency, unique IDs/names, counts, private boundary, and acyclic dependencies; negative tests prove failures are caught.

## Batch 2 — Foundation repository specifications (01–07)
For each repository, produce requirements, threat model, normative schemas/contracts, executable reference tests, and a minimal working demonstration. No repository advances beyond research/scaffolding solely on prose.

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
