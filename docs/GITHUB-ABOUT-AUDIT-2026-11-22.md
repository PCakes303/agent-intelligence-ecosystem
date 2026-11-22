# GitHub About Metadata Audit — 2026-11-22

**Scope:** 33 public account repositories (32 coordinated ecosystem repositories plus the separate PCakes303 profile repository).  
**Audit method:** Live GitHub repository metadata responses, not README or registry inference.

## Findings

| Field | Live result |
|---|---:|
| Public repositories checked | 33 |
| Non-empty descriptions | 18 |
| Blank descriptions | 15 |
| Homepage URL present | 0 |
| Topics present | 0 |

Every repository returned an empty topics array and a null homepage URL. Descriptions were present on 18 repositories and blank on 15.

## Repositories with blank descriptions

- agent-intelligence-ecosystem
- agent-ai-discovery
- mrcakes931-ecosystem
- agent-ecosystem-integration
- agent-foundation-spec
- agent-resource-manifest
- agent-schema-registry
- agent-identity-trust
- agent-secure-supply-chain
- agent-audit-provenance
- aix-core
- intelligence-knowledge-graph
- agent-tool-adapters
- agent-skill-library
- agent-sandbox-security

## Existing descriptions requiring correction or owner review

- **agent-policy-engine:** Description has topic keywords appended to descriptive prose. Move keywords into GitHub Topics and keep the description concise.
- **agent-emergency-control:** Current About description claims authenticated STOP/RESUME authority, revocation, and coordinated emergency shutdown. The implementation is explicitly a reference contract/reducer and does not yet provide authenticated authority or a live kill switch. Replace with wording that clearly describes the current scaffold and its limitations before public adoption.
- **osint-collection-framework:** Current description is awkwardly phrased and has trailing whitespace. Review for clear scope and authorized-use language.
- **osint-evidence-engine:** Current description has trailing whitespace. Keep the public-experiment marker if desired, but avoid implying guarantees not implemented.
- Review all existing descriptions for maturity accuracy; do not claim production security, live interoperability, legal compliance, or operational enforcement unless supported by evidence.

## Repository-by-repository live description status

| Repository | Description |
|---|---|
| PCakes303 (profile) | Present |
| agent-intelligence-ecosystem | Blank |
| agent-ai-discovery | Blank |
| mrcakes931-ecosystem | Blank |
| agent-ecosystem-integration | Blank |
| agent-foundation-spec | Blank |
| agent-resource-manifest | Blank |
| agent-schema-registry | Blank |
| agent-identity-trust | Blank |
| agent-secure-supply-chain | Blank |
| agent-policy-engine | Present — correction required |
| agent-audit-provenance | Blank |
| aix-core | Blank |
| aix-codecs | Present |
| agent-transport-gateway | Present |
| agent-discovery-network | Present |
| agent-capability-registry | Present |
| swarm-runtime | Present |
| swarm-coordination | Present |
| swarm-state-mesh | Present |
| osint-source-registry | Present |
| intelligence-knowledge-graph | Blank |
| agent-tool-adapters | Blank |
| agent-skill-library | Blank |
| agent-sandbox-security | Blank |
| agent-emergency-control | Present — maturity overclaim correction required |
| agent-compliance-governance | Present |
| agent-conformance-lab | Present |
| osint-collection-framework | Present — wording cleanup |
| osint-evidence-engine | Present — whitespace cleanup |
| osint-entity-resolution | Present |
| agent-federation-network | Present |
| adaptive-swarm-compression | Present |

## License metadata observation

The GitHub repository metadata reports Apache-2.0 for adaptive-swarm-compression and NOASSERTION for the other 31 ecosystem repositories; the separate profile repository returned no detected license value. This is only GitHub's repository-level license detection, not a file-level legal/provenance review. Continue the approved mixed-license review and do not infer permission from NOASSERTION.

## Owner actions

The connected GitHub integration cannot update repository About settings. For each of the 32 ecosystem repositories and the profile repository:

1. Set an accurate individualized description.
2. Set the approved master homepage URL.
3. Add relevant repository-specific topics as separate topics, not appended to the description.
4. Correct the two maturity/accuracy concerns above before treating metadata as complete.
5. Re-read the live settings and record completion.

**Disposition:** Metadata rollout is not complete. The November 5 audit is superseded by this live 33-repository snapshot.


## Owner-ready description corrections

The following wording is proposed for the 15 blank descriptions and the two descriptions that need correction. Each is intentionally capability-limited and under GitHub's 350-character description limit.

| Repository | Proposed description |
|---|---|
| agent-intelligence-ecosystem | Canonical architecture, registries, schemas, governance, and coordination control plane for the MrCakes931 Agent Intelligence Ecosystem. |
| agent-ai-discovery | Machine-readable discovery entrypoint for agent capabilities, manifests, skills, and interoperability resources across the MrCakes931 ecosystem. |
| mrcakes931-ecosystem | Public onboarding guide and navigation hub for the MrCakes931 Agent Intelligence Ecosystem, its repositories, standards, and contribution paths. |
| agent-ecosystem-integration | Versioned integration profiles and validation contracts for connecting agent tools, protocols, schemas, and policy boundaries across the ecosystem. |
| agent-foundation-spec | Normative foundation contracts for agent identity, capabilities, resources, authorization, interoperability, and secure system behavior. |
| agent-resource-manifest | Schema-backed manifests describing agent tools, skills, models, services, dependencies, permissions, and resource requirements. |
| agent-schema-registry | Versioned JSON Schema catalog and validation contracts for consistent machine-readable agent ecosystem interfaces. |
| agent-identity-trust | Contracts and validators for agent principals, identity claims, trust metadata, delegation, and revocation boundaries. |
| agent-secure-supply-chain | Validation contracts for software artifacts, dependencies, provenance, integrity metadata, and secure release workflows. |
| agent-audit-provenance | Structured audit event schemas and provenance utilities for traceable, verifiable records across agent workflows. |
| aix-core | AIX message envelope and interoperability contracts for task intent, delegation, response, status, errors, evidence, and provenance. |
| intelligence-knowledge-graph | Graph data models and bounded query utilities for representing entities, relationships, evidence, and intelligence context. |
| agent-tool-adapters | Adapter contracts and bounded invocation interfaces for exposing tools and services to AI agents under explicit policy controls. |
| agent-skill-library | Machine-readable skill manifests and validation utilities for discoverable, versioned agent skills and reusable workflows. |
| agent-sandbox-security | Fail-closed admission policy contracts and validation scaffolding for agent workloads; does not provide OS isolation or execute workloads. |
| agent-policy-engine (replace current) | Default-deny policy evaluation for agent principals, actions, resources, and scopes, with deterministic decisions and schema-backed validation. |
| agent-emergency-control (replace current) | Reference contracts and deterministic STOP/RESUME state reduction for agent systems; authenticated authority, durable distributed state, and runtime enforcement are not implemented. Not a live kill switch. |
| osint-collection-framework (replace current) | Experimental framework contracts for authorized public-information collection workflows, source handling, and adapter integration. |
| osint-evidence-engine (replace current) | Experimental evidence handling utilities for preserving source records, hashes, timestamps, provenance, and reproducibility. |

## Suggested topics for owner application

Use repository-specific topics, not one identical list everywhere. Suggested topic sets:

- Master: ai-agents, agent-ecosystem, interoperability, schemas, governance, cybersecurity, osint
- Discovery and onboarding: ai-agents, agent-discovery, capabilities, manifests, machine-readable, interoperability, open-source
- Foundation and trust: ai-agents, architecture, json-schema, identity, trust, authorization, security, standards
- Protocol and adapters: ai-agents, agent-protocol, interoperability, messaging, tool-adapters, api-contracts, authorization
- Knowledge and OSINT: knowledge-graph, entity-resolution, osint, evidence, provenance, intelligence-analysis
- Skills and sandbox: agent-skills, ai-agents, automation, workload-security, sandboxing, policy-engine, isolation-contracts
- Research: swarm-intelligence, data-compression, adaptive-compression, information-theory, distributed-systems, benchmarking

All 33 repositories still need the approved homepage URL and saved topics; re-read the live metadata after the owner applies each change.
