# MrCakes931 Agent Intelligence Ecosystem

**Status:** Portfolio provisioned and master coordination checks passing — 32 public repositories and 2 private repositories exist. All 30 public component repositories have staged master snapshots; master CI validates the portfolio registry and metadata. Production implementations, cross-repository runtime integration, package releases, and account-level security settings remain separate work.  
**Portfolio:** 34 repositories (32 public, 2 private)  
**Owner:** PCakes303 (public project identity: MrCakes931)

This repository is the canonical public control plane for the ecosystem. It owns the portfolio registry, dependency graph, shared governance, architecture decisions, compatibility overview, and public synchronization contracts. It does not replace the source repositories or duplicate their implementation code.

## Current maturity

The portfolio and architecture are approved. All 31 public ecosystem repositories and the 1 private operations repository now exist. Repository contents and maturity vary: some contain schemas, validators, examples, tests, and CI, while production services and full cross-repository conformance remain future work. Repository existence is not evidence of implementation or conformance. The registry distinguishes existence, implementation, and verification; a repository appearing there is not evidence that it is implemented or conformant.

## Start here
- [Agent Audit & Provenance](https://github.com/PCakes303/agent-audit-provenance)
- [AIX Core](https://github.com/PCakes303/aix-core)
- [AIX Codecs](https://github.com/PCakes303/aix-codecs)
- [Agent Transport Gateway](https://github.com/PCakes303/agent-transport-gateway)
- [OSINT Source Registry](https://github.com/PCakes303/osint-source-registry)
- [Intelligence Knowledge Graph](https://github.com/PCakes303/intelligence-knowledge-graph)
- [Agent Skill Library](https://github.com/PCakes303/agent-skill-library)
- [Agent Sandbox Security](https://github.com/PCakes303/agent-sandbox-security)
- [Repository 26 deployment checkpoint](checkpoints/2026-11-02-agent-sandbox-security-deployment.md)
- [Repository 26 finalization and human/security follow-up](checkpoints/2026-11-02-agent-sandbox-security-finalization.md)
- [Repository 26 open release-gates issue](https://github.com/PCakes303/agent-sandbox-security/issues/2)
- [Agent Emergency Control](https://github.com/PCakes303/agent-emergency-control) — 23 product files, exact staging parity, and CI passed on Python 3.10–3.12; contract only, not a live kill switch.
- [Repository 27 finalization checkpoint](checkpoints/2026-11-02-agent-emergency-control-finalization.md)
- [Repository 27 provisioning/build issue](https://github.com/PCakes303/agent-intelligence-ecosystem/issues/5)
- [Agent Compliance Governance](https://github.com/PCakes303/agent-compliance-governance) — 29 product files, exact staging parity, and CI passed on Python 3.10–3.12; governance scaffold only, not legal advice or certification.
- [Repository 28 release-gates issue](https://github.com/PCakes303/agent-compliance-governance/issues/2)
- [Repository 28 deployment checkpoint](checkpoints/2026-11-02-agent-compliance-governance-deployment.md)
- [Repository 28 evidence-tracker completion and back-check](checkpoints/2026-11-03-agent-compliance-governance-evidence-tracker.md)
- [Agent Conformance Lab](https://github.com/PCakes303/agent-conformance-lab) — 27 product files, exact staging parity, and CI passed 18 tests on Python 3.10–3.12; local validation scaffold, not live interoperability or certification.
- [Repository 29 release-gates issue](https://github.com/PCakes303/agent-conformance-lab/issues/2)
- [Agent Federation Network](https://github.com/PCakes303/agent-federation-network) — 17/17 product files exact-matched to staging; remote CI passed on Python 3.10–3.12. Local peer declaration validator only; no live federation.
- [Agent Conformance Lab deployment checkpoint](checkpoints/2026-11-02-agent-conformance-lab-deployment.md)
- [Portfolio-wide work review — PRs, issues, CI, staging parity and release gates](checkpoints/2026-11-02-portfolio-wide-work-review.md)

- [Adaptive Swarm Compression](https://github.com/PCakes303/adaptive-swarm-compression) — experimental data-representation and lossless codec pipeline project.\n- [Private Swarm Information Research](https://github.com/PCakes303/swarm-information-research) — restricted research headquarters; excluded from public synchronization.\n- [LLM-readable project index](llms.txt)
- [Public agent catalog — 31 repositories](registry/public-agent-catalog.json)
- [AI coding-agent instructions](AGENTS.md)
- [AI discoverability and MCP/A2A standard](docs/AI-DISCOVERABILITY.md)
- [32-repository portfolio status and work tracker](PORTFOLIO-STATUS.md)
- [GitHub repository About descriptions and topics](docs/GITHUB-REPOSITORY-ABOUT-METADATA.md)
- [Safety, emergency-stop and compliance ADR](docs/adr/0004-safety-emergency-stop-compliance.md)
- [Colorado and federal compliance management charter](docs/COMPLIANCE-MANAGEMENT-SYSTEM.md)
- [Repository 09 — policy engine](https://github.com/PCakes303/agent-policy-engine)
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
- 27 original technical repositories across foundation/security, interoperability, swarm infrastructure, OSINT/intelligence, and adoption.\n- Research expansion: `adaptive-swarm-compression` (public implementation) and `swarm-information-research` (private research authority).
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
- [AIX Core contract](specifications/aix-core/README.md), [task lifecycle](specifications/aix-core/STATE-MACHINE.md), and [experimental envelope validator](tools/validate_aix_message.py)
- [Default-deny policy prototype](prototypes/policy/README.md) and [policy-engine contract](specifications/policy-engine/README.md)
- [Audit-provenance contract](specifications/audit-provenance/README.md), [event schema](schemas/audit-provenance-event.schema.json), and [starter validator](tools/validate_audit_event.py)
- [Foundation starter learning path](docs/FOUNDATION-STARTER-PATH.md)
- [Audit event schema](schemas/audit-event.schema.json) and [hash-chain utility](tools/audit_chain.py)
- [Secure supply-chain starter contract](specifications/secure-supply-chain/README.md), [artifact schema](schemas/supply-chain-artifact.schema.json), and [validator](tools/validate_supply_chain.py)
- [Repository scaffold generator](tools/bootstrap_repositories.py)
- [Remote provisioning instructions](provisioning/README.md)


## Metadata governance

See [Capability and compatibility metadata contract](docs/CAPABILITY-COMPATIBILITY-METADATA.md).


## License status

The master registry records the intended mixed-license policy (Apache-2.0 for eligible original code and machine-readable artifacts; CC BY 4.0 for eligible original documentation). The policy is approved as a direction, but file-level contributor authority, provenance, and third-party notice review remains pending. Do not assume all files are cleared for redistribution. See [LICENSE.md](LICENSE.md) and `registry/repositories.json`.

## Current engineering readiness

The 30 public component repositories are currently specification, schema, example, validator, and starter-tooling projects at varying maturity. They are not yet installable SDK or service packages. A repository-level `manifest.json` is ecosystem metadata, not a package build manifest. Do not add empty package metadata merely to make repositories appear distributable. Add language-specific packaging only when a repository has a reusable library or executable with a defined public API, dependency policy, reproducible build, tests, and release owner. The current master audit found no standard package-build manifests across the 30 components. Cross-repository synchronization remains a target design; automated event intake, reviewed registry PR generation, scheduled reconciliation, and downstream integration execution are not yet demonstrated as deployed.

## Repository quality and maintenance standard

The mandatory public-portfolio baseline is defined in [Universal Repository Standard](docs/UNIVERSAL-REPOSITORY-STANDARD.md). Use the [Repository Cleanliness Checklist](docs/REPOSITORY-CLEANLINESS-CHECKLIST.md) for each repository audit. The [GitHub About Metadata guide](docs/GITHUB-REPOSITORY-ABOUT-METADATA.md) is a proposed settings manifest; live GitHub settings must be verified after application. See [Portfolio Status](PORTFOLIO-STATUS.md) and the dated [portfolio-wide audit checkpoint](checkpoints/2026-11-02-portfolio-wide-audit-remediation.md) for current gaps and evidence.
