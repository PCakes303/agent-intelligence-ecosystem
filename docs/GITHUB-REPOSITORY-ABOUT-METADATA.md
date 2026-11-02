# GitHub repository About metadata

**Audit date:** 2026-11-02  
**Scope:** all 23 existing public portfolio repositories (master plus 22 component repositories). The separate profile repository and private operations repository are excluded.

GitHub About metadata is separate from each repository's README and manifest. The connected GitHub integration can inspect repository metadata and update repository files, but it does not expose a repository-settings write operation for descriptions, homepage URLs, or topics. The table below is the approved, individualized metadata set to apply in each repository's **About → Edit repository details** panel.

## Verified current state

- 23 of 29 planned public portfolio repositories exist; 6 public repositories remain to be created.
- All 23 existing public portfolio repositories use the `main` default branch and have a README.
- All 23 have an empty GitHub topics list and no homepage URL.
- Nine have a description; fourteen descriptions are empty.
- `agent-policy-engine` has a malformed description because a comma-separated topic list was appended to the description field. Replace the whole field with the clean description below.
- The private operations repository and the separate `PCakes303/PCakes303` profile repository are excluded.
- A repository description or topic does not imply implementation maturity, security certification, or production readiness.

**Common homepage for all 23 public portfolio repositories:**

`https://github.com/PCakes303/agent-intelligence-ecosystem`

## Approved descriptions and topics

Use each topic as a separate GitHub topic. Do not paste the topic list into the description field.

| Portfolio # | Repository | Individualized description | Suggested topics |
|---:|---|---|---|
| 00 | [agent-intelligence-ecosystem](https://github.com/PCakes303/agent-intelligence-ecosystem) | Canonical registry, architecture decisions, dependency graph, governance and validation control plane for the MrCakes931 Agent Intelligence Ecosystem. | agentic-ai, multi-agent-systems, ecosystem-architecture, governance, dependency-management, json-schema |
| 01 | [agent-ai-discovery](https://github.com/PCakes303/agent-ai-discovery) | Machine-readable discovery documents and deterministic capability indexes that help agents and people locate authoritative ecosystem resources. | ai-agent-discovery, llms-txt, capability-index, machine-readable-metadata, agentic-ai, resource-discovery |
| 02 | [mrcakes931-ecosystem](https://github.com/PCakes303/mrcakes931-ecosystem) | Human onboarding guide to the MrCakes931 ecosystem, explaining its hybrid architecture, repository roles, security principles and contributor paths. | mrcakes931, ai-agent-ecosystem, architecture-guide, developer-onboarding, multi-agent-systems |
| 03 | [agent-ecosystem-integration](https://github.com/PCakes303/agent-ecosystem-integration) | Adapter contracts and integration profiles for connecting ecosystem components and external agent protocols without losing security or message semantics. | agent-integration, protocol-adapters, interoperability, mcp, a2a, conformance |
| 04 | [agent-foundation-spec](https://github.com/PCakes303/agent-foundation-spec) | Technology-neutral normative requirements for agent identity, trust boundaries, lifecycle, reliability, compatibility and secure system design. | agent-specification, security-requirements, trust-boundaries, reliability-engineering, interoperability, normative-contracts |
| 05 | [agent-resource-manifest](https://github.com/PCakes303/agent-resource-manifest) | JSON Schema contracts for declaring agent tools, skills, models, datasets and services with dependencies, integrity metadata and requested permissions. | resource-manifest, json-schema, agent-tools, agent-skills, permission-declaration, metadata-contract |
| 06 | [agent-schema-registry](https://github.com/PCakes303/agent-schema-registry) | Versioned JSON Schema catalog and compatibility governance for the machine-readable contracts exchanged across agent components. | schema-registry, json-schema-2020-12, schema-versioning, contract-validation, compatibility, agent-interoperability |
| 07 | [agent-identity-trust](https://github.com/PCakes303/agent-identity-trust) | Principal identity and trust contracts covering authentication context, scoped delegation, authorization boundaries, key lifecycle and revocation. | agent-identity, workload-identity, authentication-context, authorization, delegation, trust-management |
| 08 | [agent-secure-supply-chain](https://github.com/PCakes303/agent-secure-supply-chain) | Artifact-record and provenance contracts for SBOM references, source commits, digests and signature-verification evidence in agent software supply chains. | software-supply-chain, sbom, artifact-provenance, signature-verification, software-integrity, secure-builds |
| 09 | [agent-policy-engine](https://github.com/PCakes303/agent-policy-engine) | Experimental deterministic default-deny policy decision evaluator for agent principals, actions, resources and scopes, with explainable rule outcomes. | policy-decision-point, default-deny, least-privilege, agent-authorization, access-control, policy-evaluation |
| 10 | [agent-audit-provenance](https://github.com/PCakes303/agent-audit-provenance) | Portable audit-event schema and SHA-256 hash-chained JSONL reference tooling for traceability and tamper-evident event-history checks. | audit-events, hash-chain, sha256, event-provenance, forensic-readiness, audit-logging |
| 11 | [aix-core](https://github.com/PCakes303/aix-core) | Experimental Agent Interoperability eXchange semantic extension defining task, intent, capability, context, lifecycle and provenance envelopes over existing standards. | aix, agent-interoperability, semantic-envelope, mcp-extension, a2a-integration, task-lifecycle |
| 12 | [aix-codecs](https://github.com/PCakes303/aix-codecs) | RFC 8785 canonical JSON encoding and strict decoding reference implementation for deterministic AIX message serialization. | aix, rfc8785, json-canonicalization, canonical-json, deterministic-serialization, message-codec |
| 13 | [agent-transport-gateway](https://github.com/PCakes303/agent-transport-gateway) | Experimental transport-neutral request guard and integration boundary for carrying AIX messages over HTTP, MCP and A2A with bounded replay and policy checks. | agent-transport, http-gateway, mcp, a2a, replay-protection, request-validation |
| 14 | [agent-discovery-network](https://github.com/PCakes303/agent-discovery-network) | Experimental trust-filtered index for expiring agent, resource and service advertisements with injected signature-verification and trust-policy gates. | agent-discovery, service-discovery, capability-advertisement, trust-filtering, distributed-agents, discovery-index |
| 15 | [agent-capability-registry](https://github.com/PCakes303/agent-capability-registry) | Bounded local catalog that validates declared agent capabilities and matches task requirements through an advisory, policy-filtered lookup. | capability-registry, agent-capabilities, task-matching, capability-discovery, policy-filtering, agent-orchestration |
| 16 | [swarm-runtime](https://github.com/PCakes303/swarm-runtime) | Experimental bounded worker supervisor for task admission, lifecycle tracking, adapter health and policy/audit hooks; it does not provide sandbox isolation. | swarm-runtime, worker-supervisor, task-execution, admission-control, lifecycle-management, hybrid-swarm |
| 17 | [swarm-coordination](https://github.com/PCakes303/swarm-coordination) | Experimental task delegation coordinator with capability-based candidate selection, idempotency, acknowledgement binding, bounded retries and lease recovery. | swarm-coordination, task-delegation, idempotency, lease-recovery, agent-orchestration, distributed-workflows |
| 18 | [swarm-state-mesh](https://github.com/PCakes303/swarm-state-mesh) | Experimental versioned task-event and state reference with optimistic revisions, event-ID idempotency, deterministic snapshots and opaque context references. | swarm-state, event-log, optimistic-concurrency, idempotency, distributed-systems, context-references |
| 19 | [osint-source-registry](https://github.com/PCakes303/osint-source-registry) | Review-gated catalog of public information sources, datasets and APIs with licensing, permitted-purpose, access-limit, retention and approval metadata. | osint, source-catalog, data-governance, licensing, source-provenance, compliance-controls |
| 23 | [intelligence-knowledge-graph](https://github.com/PCakes303/intelligence-knowledge-graph) | Experimental provenance-aware graph model connecting source records, preserved evidence and entities through evidence-backed relationships with explicit uncertainty. | intelligence-knowledge-graph, osint, evidence-provenance, graph-model, uncertainty, relationship-analysis |
| 24 | [agent-tool-adapters](https://github.com/PCakes303/agent-tool-adapters) | Experimental dependency-free Python reference contract for explicit tool adapter registration, capability declarations, policy-gated invocation and bounded JSON payloads; no bundled third-party adapters or sandbox runtime. | agent-tool-adapters, tool-adapters, agentic-ai, capability-security, policy-gating, python, json-validation, plugin-architecture |
| 25 | [agent-skill-library](https://github.com/PCakes303/agent-skill-library) | Experimental declarative skill package format, versioned workflow schema and local validator for reusable agent workflows; no execution engine, publisher trust service or policy enforcement. | agent-skills, workflow-automation, agentic-ai, json-schema, declarative-workflows, capability-security, python |

## Application checklist

For each of the 23 repositories:

1. Open the repository page and select **About → Edit repository details**.
2. Set the exact description from the table.
3. Set the common master-repository homepage URL.
4. Add the listed topics individually.
5. Save, then re-read the repository metadata to confirm the description, homepage and topics.

For `agent-policy-engine`, replace the malformed description completely; do not append or retain the comma-separated topics in that field.

## Maturity and licensing guardrails

- Descriptions intentionally use **experimental** or **reference** where appropriate and do not imply production certification.
- Discovery and capability matching are advisory; neither authenticates an agent nor grants permission.
- The Swarm Runtime is not a sandbox. The Transport Gateway is not yet a production network gateway.
- The OSINT Source Registry catalogs metadata only; it does not collect or crawl source content.
- The Knowledge Graph does not collect evidence, resolve real-world identities, or assert truth.
- Repository-specific license selection remains pending portfolio review. Do not add license files or claim a license until the mixed-license decision is approved.

## Audit boundary

This metadata file is the canonical set of recommended GitHub About values. It is not evidence that those values have been applied. The GitHub connector available in this workflow supports repository reads and file commits, but not writes to repository description, homepage or topics settings; those settings must be applied in GitHub's repository UI.
