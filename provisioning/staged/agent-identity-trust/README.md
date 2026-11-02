# Agent Identity and Trust

**MrCakes931 Agent Intelligence Ecosystem · Identity and security layer**

Defines principal identity, authentication context, authorization, delegation, revocation, and trust-boundary contracts for agents, services, workloads, and human operators.

## Scope
- Issuer-scoped principal identifiers for human, agent, service, and workload identities.
- Credential metadata, audience and validity constraints.
- Default-deny authorization and narrowly scoped delegation.
- Key rotation, expiry, revocation, and security audit requirements.

## Layout
- schemas/principal.schema.json — principal data contract.
- examples/principal.json — illustrative principal record.
- docs/IDENTITY-TRUST.md — security and interoperability model.
- tools/validate_principal.py — standard-library record validator.
- tests/ — automated validation tests.
- .github/workflows/validate.yml — CI validation.

## Validate locally
Requires Python 3.10+. Install the pinned development schema-validator dependency:

    python -m pip install -r requirements-dev.txt
    python tools/validate_principal.py
    python -m unittest discover -s tests -v

## Trust model
A principal identifier names an entity within an issuer's namespace. It is not proof of authentication, authorization, or human ownership. Authentication must validate credentials and issuer, audience, validity interval, and intended use. Authorization is evaluated per action and resource, defaults to deny, and fails closed. Delegation must be constrained by action, resource, audience, and expiry. Revocation and key rotation must be supported.

SPIFFE/SPIRE, OAuth 2.0, and OpenID Connect are integration targets. This repository does not yet operate an identity provider or issue credentials.

## License status

This repository applies a scoped mixed-license policy: original source code and machine-readable contracts are licensed under Apache-2.0; original human-readable documentation is licensed under CC BY 4.0. Third-party material retains upstream terms. Datasets, evidence, fixtures, sample payloads, media, and material with uncertain provenance are not blanket-licensed and require separate review. See [LICENSE.md](LICENSE.md).

## Status
Scaffolded, v0.1.0. Published data contract, example, reference validator, tests, and CI are an initial foundation, not a deployed trust service.

## Entry-level build

Start with the runnable starter build:

    python tools/starter_build.py
    python -m unittest discover -s tests -v

See [Entry-level build guide](docs/ENTRY-LEVEL-BUILD.md) for Starter → Developer → Production progression.

## Ecosystem
Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem

Public project identity: **MrCakes931**  
GitHub owner: `PCakes303`

