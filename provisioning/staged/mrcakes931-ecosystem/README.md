# MrCakes931 Agent Intelligence Ecosystem

Welcome to the human-facing guide for the **MrCakes931 Agent Intelligence Ecosystem**, a coordinated 32-repository portfolio (31 public repositories and one private operations repository) for interoperable, secure, distributed agent systems and supporting intelligence workflows.

**Public identity:** MrCakes931  
**GitHub owner:** PCakes303  
**Master registry:** [agent-intelligence-ecosystem](https://github.com/PCakes303/agent-intelligence-ecosystem)  
**This repository's role:** human onboarding and navigation; not the canonical machine-readable registry.

## What the ecosystem is

The ecosystem combines a shared control plane with independently developed components. It uses a hybrid swarm architecture: centralized publication of common metadata and contracts, federated operational domains, and peer-to-peer exchange where justified. It extends and composes existing standards rather than attempting to replace them.

## Start here

- [Architecture overview](docs/ARCHITECTURE.md)
- [Getting started and contribution paths](docs/ONBOARDING.md)
- [Repository map](docs/REPOSITORY-MAP.md)
- [Canonical repository registry](https://github.com/PCakes303/agent-intelligence-ecosystem/blob/main/registry/repositories.json)
- [Canonical dependency graph](https://github.com/PCakes303/agent-intelligence-ecosystem/blob/main/registry/dependencies.json)
- [Foundation implementation packet](https://github.com/PCakes303/agent-intelligence-ecosystem/blob/main/docs/FOUNDATION-IMPLEMENTATION-PACKET.md)

## Architecture at a glance

| Layer | Responsibility |
|---|---|
| Control plane | Repository registry, dependencies, governance, compatibility |
| Discovery and guide | Machine-readable discovery and human navigation |
| Foundation/security | Vocabulary, schemas, manifests, identity, authorization, audit, supply chain |
| Protocols | AIX semantic extension, codecs, secure transport integration |
| Swarm | Discovery, capabilities, runtime, coordination, state mesh |
| Intelligence | Public source catalogue, authorized collection, evidence, entity resolution, graph |
| Adoption/federation | Tool adapters, skills, sandboxing, conformance, independent federation |
| Private operations | Restricted planning and security operations, excluded from public sync |

## Core principles

- **AIX is an extension layer**, not a replacement for MCP, A2A, or existing standards.
- **Hybrid swarm:** shared coordination contracts with independent trust domains and federated nodes.
- **Default deny and least authority:** discovery is not trust; authentication is not authorization.
- **Evidence over claims:** planned, implemented, tested, and released are distinct states.
- **Separation of ownership:** each component repo owns its implementation; the master owns the ecosystem index.
- **Privacy boundary:** private operations remain private and are never automatically exported to public repositories.

## Repository maturity

The master registry is the source of truth for repository existence, visibility, dependencies, and maturity. A link in this guide does not imply that the repository has been created or implemented. Repository maturity labels are defined in [ONBOARDING.md](docs/ONBOARDING.md).

## Contributing

Choose the component repository that owns the behavior you intend to change. Read its README, AGENTS.md, CONTRIBUTING.md, and SECURITY.md. Include tests and evidence; do not commit secrets or private operational information.

## Status

This guide is an initial documentation scaffold with architecture, onboarding, and repository navigation pages. The component implementations and integrations are being built incrementally; consult the master registry and each repository's CI/release evidence before relying on a capability.

## Entry-level build

Start with the runnable starter build:

    python tools/starter_build.py
    python -m unittest discover -s tests -v

See [Entry-level build guide](docs/ENTRY-LEVEL-BUILD.md) for Starter → Developer → Production progression.

## License

This repository documents the ecosystem's intended scoped mixed-license policy: Apache-2.0 for eligible original code and machine-readable contracts, and CC BY 4.0 for eligible original human-readable documentation. Its manifest remains `pending-review` until contributor authority, file-level provenance and third-party notices are checked. Do not assume every file is cleared for redistribution. Third-party material retains upstream terms; data, evidence, fixtures, sample payloads and media receive no blanket license. See [LICENSE.md](LICENSE.md).
