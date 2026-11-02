# GitHub repository About metadata

The README and manifest do not populate GitHub's repository-level **About** description, website, or topics. The GitHub connector used for this work can read repository metadata and commit files, but it does not expose the repository-settings update operation. Use the descriptions and topics below in each repository's GitHub **Settings / General → About** area.

Descriptions are intentionally concise and distinguish each component's role. They do not imply production maturity.

| # | Repository | Description | Suggested topics |
|---:|---|---|---|
| 00 | [agent-intelligence-ecosystem](https://github.com/PCakes303/agent-intelligence-ecosystem) | Master registry, architecture, governance, dependency graph, and validation control plane for the MrCakes931 agent ecosystem. | agentic-ai, multi-agent-systems, ecosystem, governance, architecture, json-schema |
| 01 | [agent-ai-discovery](https://github.com/PCakes303/agent-ai-discovery) | AI-native discovery metadata, machine-readable capability indexes, and agent integration entry points for the MrCakes931 ecosystem. | ai-agents, agent-discovery, llms-txt, agentic-ai, metadata, interoperability |
| 02 | [mrcakes931-ecosystem](https://github.com/PCakes303/mrcakes931-ecosystem) | Human-facing guide to the MrCakes931 Agent Intelligence Ecosystem, its architecture, repositories, and onboarding path. | ai-agents, documentation, ecosystem, multi-agent-systems, onboarding |
| 03 | [agent-ecosystem-integration](https://github.com/PCakes303/agent-ecosystem-integration) | Integration profiles, adapter contracts, and conformance guidance for interoperating components in the MrCakes931 agent ecosystem. | ai-agents, interoperability, integration, conformance, agentic-ai |
| 04 | [agent-foundation-spec](https://github.com/PCakes303/agent-foundation-spec) | Normative foundation requirements and shared security, lifecycle, reliability, and compatibility contracts for AI agent systems. | ai-agents, specifications, security, reliability, standards, agentic-ai |
| 05 | [agent-resource-manifest](https://github.com/PCakes303/agent-resource-manifest) | Machine-readable manifests for agent tools, skills, models, datasets, services, dependencies, and requested permissions. | ai-agents, manifests, json-schema, tools, skills, metadata |
| 06 | [agent-schema-registry](https://github.com/PCakes303/agent-schema-registry) | Versioned JSON Schema catalog and governance conventions for machine-readable contracts across agent systems. | json-schema, schema-registry, ai-agents, validation, interoperability |
| 07 | [agent-identity-trust](https://github.com/PCakes303/agent-identity-trust) | Identity and trust contracts for agent principals, authentication context, authorization, delegation, and revocation. | ai-agents, identity, trust, authorization, security, delegation |
| 08 | [agent-secure-supply-chain](https://github.com/PCakes303/agent-secure-supply-chain) | Artifact integrity, SBOM references, source provenance, and signature-verification contracts for secure agent software supply chains. | supply-chain-security, sbom, provenance, artifact-integrity, software-security, ai-agents |
| 09 | [agent-policy-engine](https://github.com/PCakes303/agent-policy-engine) | Default-deny authorization policies and deterministic decision evaluation for agent identities, actions, resources, and scopes. | ai-agents, policy-engine, authorization, access-control, least-privilege, security |

## Repo 08 and 09 readiness

**08 — agent-secure-supply-chain:** repository files and starter CI exist; latest recorded starter CI passed. Its About description and topics remain unset. Its validator is being tightened with malformed-host and credential-bearing URL rejection tests. It remains scaffolding, not a signature verifier or SBOM generator.

**09 — agent-policy-engine:** not yet created on GitHub. A repository-specific starter is being prepared under `provisioning/staged/agent-policy-engine/`. Create the public GitHub repository with this exact name, empty (no README/license/gitignore initialization), then the staged files can be copied into it and CI run. The GitHub About description above is ready to paste.

## Homepage field

For component repositories, use the master registry as the homepage:
https://github.com/PCakes303/agent-intelligence-ecosystem

The private operations repository is intentionally excluded. The separate profile repository is not part of the 30-repository portfolio.
