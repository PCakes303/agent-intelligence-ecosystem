# MrCakes931 Agent Intelligence Ecosystem

**Status:** Phase 0 — architecture and control-plane initialization  
**Portfolio:** 30 repositories (29 public, 1 private)  
**Owner:** PCakes303 (public project identity: MrCakes931)

This repository is the canonical public control plane for the ecosystem. It owns the portfolio registry, dependency graph, shared governance, architecture decisions, compatibility overview, and public synchronization contracts. It does not replace the source repositories or duplicate their implementation code.

## Current maturity

The portfolio and architecture are approved. Repository implementation is **planned** until independently verified. A repository appearing in the registry is not evidence that it exists, is implemented, or is conformant.

## Start here

- [Architecture](docs/ARCHITECTURE.md)
- [Repository registry](registry/repositories.json)
- [Dependency graph](registry/dependencies.json)
- [Governance](GOVERNANCE.md)
- [Security baseline](SECURITY.md)
- [Synchronization design](docs/SYNCHRONIZATION.md)
- [Roadmap](ROADMAP.md)
- [Architecture decisions](docs/adr/)

## Operating principles

1. Specifications and interfaces before implementation.
2. Reuse established standards; define extensions only where a demonstrated gap exists.
3. Every repository owns its implementation; this master repository owns the ecosystem index.
4. Changes are validated and proposed as reviewed updates, not blindly copied.
5. Public automation must never ingest private content.
6. Claims of capability must be supported by tests, evidence, and release metadata.
7. Security, privacy, provenance, accessibility, and operational resilience are design requirements.

## Portfolio layout

- Ecosystem control plane: this repository.
- AI-native discovery: `agent-ai-discovery`.
- Human-facing ecosystem guide: `mrcakes931-ecosystem`.
- Cross-repository integration: `agent-ecosystem-integration`.
- 25 technical repositories across foundation/security, interoperability, swarm infrastructure, OSINT/intelligence, and adoption.
- One private operational repository: `agent-ecosystem-private`.

See the registry for authoritative names, visibility, scope, status, and dependencies.

## Naming and ownership

GitHub owner remains `PCakes303` until formally changed. Public-facing project identity is `MrCakes931`. The separate profile repository `PCakes303/PCakes303` is not the ecosystem master and is not managed by this portfolio registry.

## Entry-level build

Install the pinned development dependency and run the first reproducible build:

```bash
python -m pip install -r requirements-dev.txt
python tools/starter_build.py
```

See [Entry-level build guide](docs/ENTRY-LEVEL-BUILD.md) for Starter → Developer → Production progression.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md), open an issue for substantial changes, and use pull requests for reviewed modifications. Do not publish secrets, private research, personal data, or embargoed vulnerability details.

## Working prototypes and tooling

- [Resource manifest schema](schemas/agent-resource.schema.json) and [validator](tools/validate_agent_resource.py)
- [AIX experimental envelope](prototypes/aix/aix-message.schema.json)
- [Default-deny policy prototype](prototypes/policy/README.md)
- [Audit event schema](schemas/audit-event.schema.json) and [hash-chain utility](tools/audit_chain.py)
- [Secure supply-chain starter contract](specifications/secure-supply-chain/README.md), [artifact schema](schemas/supply-chain-artifact.schema.json), and [validator](tools/validate_supply_chain.py)
- [Repository scaffold generator](tools/bootstrap_repositories.py)
- [Remote provisioning instructions](provisioning/README.md)
