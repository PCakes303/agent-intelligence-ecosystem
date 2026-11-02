# Foundation repositories 01–07: implementation packet

**Status:** planned implementation packet  
**Baseline contract:** `contracts/foundation/README.md` v1.0.0  
**Requirement catalogue:** `contracts/foundation/requirements.json`

This packet turns the shared contract into buildable, independently verifiable repository work. It is not evidence that the remote repositories exist or that any implementation has shipped.

## Build order and exit criteria

### 01 — agent-foundation-spec

**Authority:** normative architecture vocabulary, lifecycle, requirement model, compatibility policy, ADR process.

Deliver:
- glossary and principal/resource/action/context vocabulary;
- lifecycle states for agent, capability, credential, task, and release;
- requirement and conformance language;
- trust-boundary and failure-mode reference diagrams;
- compatibility and deprecation policy;
- ADR template and decision index.

Exit criteria:
- every normative statement has a stable requirement ID;
- all terms used by other foundation contracts are defined once;
- conformance levels distinguish documentation, interface, and tested behavior;
- security review confirms no implicit trust from discovery or network position.

### 02 — agent-schema-registry

**Authority:** schema publication, identifiers, versioning, validation, and compatibility.

Deliver:
- canonical schema metadata and immutable version identifiers;
- JSON Schema 2020-12 validation pipeline;
- compatibility classification rules and machine-readable reports;
- positive, negative, boundary, and fuzz test fixtures;
- deprecation and migration examples.

Exit criteria:
- schema IDs are globally unique within the ecosystem namespace;
- invalid fixtures are rejected with actionable diagnostics;
- breaking changes are detected or explicitly declared;
- schemas are validated against the foundation vocabulary.

### 03 — agent-resource-manifest

**Authority:** descriptive metadata for agents, tools, services, repositories, and datasets.

Deliver:
- manifest schema and examples by resource type;
- stable resource identifiers and publisher metadata;
- declared capabilities, interfaces, versions, and external references;
- data classification, retention, provenance, and usage constraints;
- signature/provenance reference fields where available.

Exit criteria:
- manifests validate against a pinned schema version;
- publisher and resource identity are distinguishable;
- capability declarations are descriptive only and cannot grant authorization;
- consumers can detect stale or incompatible manifests.

### 04 — agent-identity-trust

**Authority:** principal identity, workload identity, authentication, trust domains, credential lifecycle, revocation.

Deliver:
- principal and trust-domain model;
- authentication profile mapping (OIDC and SPIFFE/SPIRE where appropriate);
- credential issuance, rotation, expiry, revocation, and compromise procedures;
- audience and subject binding rules;
- federation and trust-on-first-use exclusions;
- threat model and interoperability tests.

Exit criteria:
- principals are unambiguously scoped to an issuer and trust domain;
- expired, revoked, wrong-audience, and wrong-subject credentials fail;
- trust is not inferred from discovery, DNS, IP address, or repository membership;
- secrets are not committed to source.

### 05 — agent-policy-engine

**Authority:** authorization vocabulary, policy decision contract, evaluation semantics, enforcement guidance.

Deliver:
- subject/action/resource/context decision model;
- default-deny reference semantics;
- policy version and decision provenance;
- capability scope, expiry, audience, delegation depth, and constraints;
- OPA integration profile or documented alternative;
- policy test vectors and enforcement examples.

Exit criteria:
- missing, malformed, unavailable, or indeterminate policy decisions deny protected operations;
- policy decisions are bound to principal, action, resource, context, and policy version;
- enforcement occurs at the protected resource boundary;
- tests cover allow, deny, conflict, expiry, and policy-unavailable cases.

### 06 — agent-audit-provenance

**Authority:** audit event schema, provenance references, integrity protection, verification.

Deliver:
- versioned audit event schema;
- event correlation and causal reference conventions;
- actor, action, target, outcome, policy, and timestamp fields;
- append-only storage interface and integrity checkpoints;
- signing and verification profile;
- privacy, retention, redaction, and export guidance.

Exit criteria:
- critical security events have required actor/action/target/outcome attribution;
- integrity verification detects modification relative to a trusted checkpoint;
- docs clearly distinguish integrity from truth and completeness;
- secrets and unnecessary sensitive payloads are excluded.

### 07 — agent-secure-supply-chain

**Authority:** source/dependency controls, build provenance, SBOM, artifact signing and release verification.

Deliver:
- dependency pinning and update policy;
- SBOM generation and validation;
- build provenance and artifact attestation workflow;
- signing identity and verification policy;
- vulnerability intake, triage, remediation, and disclosure process;
- release checklist and reproducibility evidence.

Exit criteria:
- release artifacts have a traceable source revision and build identity;
- SBOMs are attached to release artifacts;
- signatures and provenance can be verified independently;
- workflows use least privilege and short-lived credentials where supported;
- secret scanning and dependency scanning run on pull requests and default branch.

## Cross-repository contract tests

The integration layer MUST eventually test these flows end-to-end:

1. **Describe then authorize:** publish a manifest, discover the resource, authenticate its caller, and independently authorize an operation. A manifest or discovery result alone must never grant access.
2. **Authenticate then revoke:** authenticate a workload, revoke or expire its credential, and verify subsequent protected operations fail.
3. **Policy decision then audit:** evaluate allow and deny cases and verify the decision and enforcement outcome are attributable in the audit stream.
4. **Build then verify:** produce an artifact, SBOM, and provenance statement; verify the signature and source/build binding.
5. **Schema evolution:** publish a compatible additive version and a breaking version; verify compatibility classification and consumer behavior.

## Required evidence per repository

A repository is not considered implemented merely because it contains documentation. Before it can move from scaffolding to experimental, it must contain:
- a versioned contract or interface;
- at least one executable reference implementation or validator;
- positive and negative automated tests;
- reproducible local developer instructions;
- CI that runs the tests and validates schemas;
- a threat model or documented security analysis;
- a manifest declaring maturity, dependencies, and supported versions.

Before alpha, add integration tests with at least one downstream consumer, security review findings, release provenance, and migration guidance.

## Dependency sequence

The intended build sequence is:

`01 foundation-spec → 02 schema-registry → 03 resource-manifest → 04 identity-trust → 05 policy-engine → 06 audit-provenance → 07 secure-supply-chain`

This is a work sequence, not a strict one-way dependency graph. Identity and policy concepts are developed in parallel after the vocabulary and schema foundations stabilize; the supply-chain repository consumes identity and audit contracts.

## Open decisions (must be resolved by ADR)

- Which workload identity profile is the first mandatory conformance target: SPIFFE/SPIRE, OIDC workload identity, or a defined combination?
- Is OPA the normative policy engine integration or one supported reference adapter?
- Which signing and provenance profile is required for alpha releases?
- What is the minimum interoperable audit event set, and which fields are deployment-specific?
- Which repository owns the canonical JSON Schema meta-validation workflow versus reusing a central workflow?

No open decision may be resolved by embedding credentials, weakening default-deny behavior, or silently creating a proprietary replacement for an established standard.
