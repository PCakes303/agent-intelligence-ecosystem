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
