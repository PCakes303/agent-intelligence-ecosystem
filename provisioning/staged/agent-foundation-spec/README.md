# Agent Foundation Specification

**MrCakes931 Agent Intelligence Ecosystem · Foundation layer**

Defines shared, technology-neutral requirements and invariants consumed by the ecosystem's other repositories. It is the baseline for security, interoperability, reliability, lifecycle, and engineering discipline.

## Scope
- Normative requirements with stable identifiers and MUST / SHOULD / MAY priority.
- Trust-boundary, least-privilege, and fail-closed invariants.
- Versioning, compatibility, provenance, and distributed-systems expectations.
- Traceability from requirement to architecture decision, implementation, test, and verification.

## Layout
- requirements/requirements.json — machine-readable requirement catalog.
- docs/FOUNDATION-CONTRACT.md — normative principles and change process.
- tools/validate_requirements.py — standard-library validator.
- tests/ — automated validator tests.
- .github/workflows/validate.yml — CI validation.
- AGENTS.md — AI and contributor operating instructions.

## Validate locally
Requires Python 3.10+; no third-party packages are needed.

    python tools/validate_requirements.py
    python -m unittest discover -s tests -v

## Design invariants
1. Identify and validate all trust-boundary inputs.
2. Default to deny; authorization failures fail closed.
3. Version published interfaces and document breaking changes.
4. Preserve provenance; a hash proves byte equality against a trusted reference, not truth or completeness.
5. Design distributed execution around idempotency, bounded retries, and partial failure—not exactly-once claims.
6. Require human review for consequential decisions.

## Status and governance
Scaffolded, v0.1.0. The initial requirements are published and validated by CI. This does not certify downstream implementations. Normative changes require rationale, compatibility impact assessment, affected-repository review, and tests.

## Entry-level build

Start with the runnable starter build:

    python tools/starter_build.py
    python -m unittest discover -s tests -v

See [Entry-level build guide](docs/ENTRY-LEVEL-BUILD.md) for Starter → Developer → Production progression.

## Ecosystem
Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem

Public project identity: **MrCakes931**  
GitHub owner: `PCakes303`

## Licensing

This repository documents the ecosystem's intended scoped mixed-license policy: Apache-2.0 for eligible original code and machine-readable contracts, and CC BY 4.0 for eligible original human-readable documentation. Its manifest remains `pending-review` until contributor authority, file-level provenance and third-party notices are checked. Do not assume every file is cleared for redistribution. Third-party material retains upstream terms; data, evidence, fixtures, sample payloads and media receive no blanket license. See [LICENSE.md](LICENSE.md).
