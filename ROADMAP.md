# Roadmap

**Status date:** 2026-11-05  
**Portfolio:** 34 repositories total — 32 public and 2 private, including the original ecosystem portfolio and the research expansion.

This roadmap distinguishes repository provisioning from implementation, integration, and production readiness. A repository's existence, README, manifest, tests, or green CI does not by itself mean its service is operational or production-ready.

## Phase 0 — Portfolio and control plane

**Provisioning: complete.**

- [x] Provision the master control-plane repository and all 30 public component repositories.
- [x] Provision the separate private operations repository.
- [x] Publish the canonical 34-entry repository inventory (32 public, 2 private) and 32-entry public-only catalog.
- [x] Maintain dependency graph, manifest schema, architecture decisions, governance, and repository standards.
- [x] Create a master staging snapshot for each of the 31 public component repositories.
- [x] Verify live-to-staged manifest blob parity for all 31 public components.
- [x] Verify the three recently added original snapshots by exact recursive path/blob comparison.
- [x] Add the adaptive-swarm-compression snapshot and verify exact 28/28 path/blob parity.
- [x] Validate repository inventory, IDs, dependency references, capability/compatibility metadata, and README license-status consistency in master CI.
- [x] Pass the latest master CI run: 22 jobs, 53 tests, seven component staging matrices across Python 3.10–3.12.
- [ ] Complete human-owned GitHub account settings, branch rules, security features, and repository About metadata verification.
- [ ] Complete file-level licensing, contributor-authority, provenance, and third-party notice review.

## Phase 1 — Foundation and cybersecurity

**Provisioning: complete; implementation and assurance: partial.**

Repositories: `agent-foundation-spec`, `agent-resource-manifest`, `agent-schema-registry`, `agent-identity-trust`, `agent-secure-supply-chain`, `agent-policy-engine`, and `agent-audit-provenance`.

Existing work includes normative drafts, JSON Schemas, validators, fixtures, tests, and starter tooling at varying levels of maturity.

Exit gates:
- [ ] Trace normative requirements to executable acceptance tests.
- [ ] Demonstrate authenticated identity issuance, rotation, delegation, and revocation.
- [ ] Integrate policy decisions with authenticated principal and resource context; demonstrate enforcement at a real boundary.
- [ ] Generate and verify SBOMs, provenance attestations, signatures, and dependency-policy results.
- [ ] Add authenticated audit ingestion, signed checkpoints, retention controls, and identity integration.
- [ ] Run cross-repository contract tests against pinned versions and negative security cases.

## Phase 2 — Protocols and communication

**Provisioning: complete; interoperability: experimental / partial.**

Repositories: `aix-core`, `aix-codecs`, and `agent-transport-gateway`.

AIX remains an extension/interoperability layer over established standards, not a replacement for MCP, A2A, HTTP, OpenAPI, or JSON Schema.

Exit gates:
- [ ] Publish explicit, versioned MCP and A2A mapping profiles.
- [ ] Add cross-language canonicalization and codec vectors.
- [ ] Demonstrate authenticated transport, authorization, replay resistance, and bounded payload handling.
- [ ] Measure semantic translation fidelity, latency, validation cost, and failure behavior.
- [ ] Run independent interoperability tests with external implementations.

## Phase 3 — Discovery and swarm infrastructure

**Provisioning: complete; distributed runtime: partial / not production-ready.**

Repositories: `agent-discovery-network`, `agent-capability-registry`, `swarm-runtime`, `swarm-coordination`, and `swarm-state-mesh`.

The approved topology is hybrid: centralized, federated, and peer-to-peer, selected according to workload and trust boundaries.

Exit gates:
- [ ] Demonstrate authenticated discovery and capability publication.
- [ ] Specify and test idempotency, bounded retries, leases, timeouts, backpressure, and partition recovery.
- [ ] Establish consistency and conflict-resolution semantics per state type.
- [ ] Add failure-injection, replay, duplicate-delivery, node-churn, and malicious-peer tests.
- [ ] Prove authorization and emergency-stop enforcement across nodes before enabling privileged workloads.

## Phase 4 — OSINT and intelligence

**Provisioning: complete; operational collection and intelligence pipeline: gated.**

Repositories: `osint-source-registry`, `osint-collection-framework`, `osint-evidence-engine`, `osint-entity-resolution`, and `intelligence-knowledge-graph`.

Current validators and contracts do not constitute a live collection pipeline. Collection remains disabled until authorization, source-use, privacy, safety, evidence, and emergency-control gates are independently demonstrated.

Exit gates:
- [ ] Validate source permissions, terms, rate limits, access controls, and collection authorization.
- [ ] Implement authenticated collection provenance and controlled evidence storage.
- [ ] Add integrity-protected evidence records, trusted timestamps, retention and access controls.
- [ ] Validate entity-resolution accuracy, uncertainty, bias, and human-review requirements; retain the approved non-personal scope unless separately reviewed.
- [ ] Add graph write authorization, provenance links, and correction/deletion workflows.
- [ ] Complete qualified privacy and legal review for each deployment and data category.

## Phase 5 — Adoption, integration, and conformance

**Provisioning: complete; end-to-end integration: partial / not production-ready.**

Repositories: `agent-tool-adapters`, `agent-skill-library`, `agent-sandbox-security`, `agent-conformance-lab`, `agent-federation-network`, `agent-ai-discovery`, `mrcakes931-ecosystem`, and `agent-ecosystem-integration`.

Existing components are at different levels: discovery and guide material, adapters and skills, local sandbox policy contracts, local conformance validators, peer declaration validation, and integration scaffolding. They do not yet constitute a production integrated runtime.

Exit gates:
- [ ] Implement real OS-level sandbox isolation and verify filesystem, process, network, resource, and escape boundaries.
- [ ] Implement authenticated peer identity, cryptographic signature validation, authorization, revocation, replay resistance, and secure transport.
- [ ] Implement reviewed cross-repository synchronization: authenticated event intake, immutable-SHA manifest validation, allowlisted registry-update PRs, scheduled reconciliation, and operational alerts.
- [ ] Build pinned integration fixtures across foundation, AIX, swarm, safety, OSINT, and federation components.
- [ ] Run independent end-to-end conformance suites and publish reproducible evidence; do not call local validators certification.
- [ ] Demonstrate at least two independently operated federation peers before claiming federation capability.

## Phase 6 — Emergency control and compliance governance

**Provisioning: complete; enforcement and legal applicability: not yet demonstrated.**

Repositories: `agent-emergency-control` and `agent-compliance-governance`. These are cross-cutting requirements, not optional add-ons.

Exit gates:
- [ ] Authenticate emergency-stop authority and cryptographically verify commands.
- [ ] Demonstrate monotonic STOP behavior, durable state, revocation, independent administration, and controlled RESUME.
- [ ] Demonstrate stop propagation and enforcement at every relevant runtime, adapter, sandbox, swarm, collection, and federation boundary.
- [ ] Collect control evidence with accountable owners, timestamps, review status, and retention.
- [ ] Have qualified counsel determine applicable Colorado, federal, and other deployment-specific legal obligations; do not infer compliance from a control catalog.
- [ ] Keep privileged/untrusted execution and OSINT collection disabled until applicable gates are met.

## Cross-cutting release engineering

The portfolio is currently a collection of specifications, schemas, validators, examples, and starter tools at varying maturity. It is **not** a set of 30 installable SDK or service packages.

- [x] Audit all 30 public component roots for standard package-build metadata; no `pyproject.toml`, `package.json`, `Cargo.toml`, `go.mod`, or equivalent package manifest was found.
- [ ] Do not add empty or arbitrary package metadata solely for uniformity.
- [ ] When a component has a reusable library or executable with a stable public API, select its language and packaging model, then add reproducible builds, dependency locks, SBOM, artifact signing, and install-from-artifact tests.
- [ ] Define release ownership, semantic versioning, compatibility windows, deprecation policy, and artifact retention.
- [ ] Pin third-party CI actions, minimize workflow token permissions, and verify branch protections and required checks.
- [ ] Complete item-level licensing and provenance review before publishing distributable artifacts.

## Completion criteria

The portfolio is considered **provisioned** when all 32 repositories exist and the public registry accurately describes them. It is considered **coordinated** when manifests, dependency references, staging snapshots, catalogs, and CI remain synchronized. It is considered **integrated** only when pinned cross-repository tests pass against real implementations. It is considered **production-ready** only after security, operational, legal, privacy, resilience, and independent verification gates are evidenced.

A phase is not complete merely because documentation or repository scaffolding exists. Every milestone report must state implementation scope, tests, evidence, limitations, risks, affected dependencies, and next gate.


## Phase 7 — Swarm-native information representation research

**Provisioning: complete; implementation: experimental; distributed research outcomes: not yet validated.**

Repositories:
- Public: [adaptive-swarm-compression](https://github.com/PCakes303/adaptive-swarm-compression)
- Private research remains in a separate restricted workspace and is not listed in public discovery.

The private repository is the research authority for hypotheses, taxonomies, experiment design, negative results, and architecture decisions. It is excluded from public synchronization. The public implementation currently provides a local lossless codec pipeline foundation, exact reconstruction checks, a representation-capsule schema, and a Python test workflow.

Exit gates:
- [ ] Verify GitHub Actions across Python 3.10–3.12.
- [ ] Add reproducible baseline benchmarks with complete storage, transfer, compute, metadata, and coordination accounting.
- [ ] Validate representation capsule schemas and version compatibility.
- [ ] Build constrained workload-aware pipeline composition.
- [ ] Evaluate shared dictionaries and cross-agent deduplication with all distribution and synchronization overhead included.
- [ ] Implement selective reconstruction and compare with decoded reference results.
- [ ] Prototype compute-on-encoded-data operations for explicitly supported formats.
- [ ] Add privacy, tenant-isolation, provenance, resource-exhaustion, and adversarial-input tests before distributed deployment.
- [ ] Publish only individually reviewed, reproducible findings from restricted research when explicitly approved.


## Phase 6 — Research and data representation

**Provisioning: complete; local implementation: experimental; distributed research: not yet implemented.**

Public implementation: `adaptive-swarm-compression`. Restricted research material is maintained separately and is not a dependency or public discovery source.

Current public foundation includes identity and zlib lossless codecs, ordered local pipeline execution, source digest verification, bounded decompression, a representation-capsule schema, deterministic synthetic workloads, a local benchmark runner, and regression tests.

Exit gates:
- [ ] Verify remote CI on Python 3.10, 3.11, and 3.12.
- [ ] Validate the representation-capsule schema in CI and define compatibility/versioning rules.
- [ ] Publish repeated baseline measurements with complete local accounting and reproducibility details.
- [ ] Decide and apply an explicit license before inviting external reuse or contributions.
- [ ] Add cross-repository conformance tests; exact 28/28 master-staging parity is already verified.
- [ ] Implement constrained pipeline selection with declared stage preconditions, resource limits, and exactness guarantees.
- [ ] Prototype chunked selective reconstruction and compare it with full reconstruction.
- [ ] Evaluate shared dictionaries only after accounting for distribution, synchronization, trust-boundary, and recovery costs.
- [ ] Demonstrate a measurable benefit over conventional baselines before adding distributed swarm coordination.
