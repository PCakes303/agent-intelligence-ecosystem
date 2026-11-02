# ADR 0001: Portfolio Architecture

- Status: Accepted
- Date: 2026-11-01
- Decision owners: MrCakes931 ecosystem maintainers

## Context

The project requires a coherent multi-repository ecosystem with independently maintainable components, cross-repository integration, public discoverability, human onboarding, and a protected internal workspace.

## Decision

Adopt a 30-repository portfolio: one public master control plane, three additional public ecosystem-level repositories, 25 public technical repositories, and one private operations repository. AIX is an extension/interoperability layer; swarm topology is hybrid; licensing is mixed by artifact/repository; the full intended architecture may be published with honest maturity labels.

## Alternatives considered

- One monorepo: rejected for the current portfolio because independent release and ownership boundaries are valuable.
- Fully decentralized registries: rejected as the sole approach because ecosystem-wide compatibility and dependency views need a canonical index.
- Master repository owns all source: rejected because it creates coupling and duplicates repository authority.
- Private data mirrored into public registry: rejected due to information-flow risk.

## Consequences

The master registry must remain accurate, schema-validated, and provenance-aware. Cross-repository automation is required, but must use reviewed pull requests and strict public/private separation. The private repository is not a dependency of public builds.
