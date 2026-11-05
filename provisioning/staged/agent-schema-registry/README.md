# Agent Schema Registry

**MrCakes931 Agent Intelligence Ecosystem · Contract layer**

A versioned catalog of JSON Schemas and compatibility rules for ecosystem manifests, messages, identities, and audit records. The registry makes contracts discoverable, reviewable, and evolvable without coupling consumers to a single runtime.

## Scope
- JSON Schema Draft 2020-12 as the default dialect.
- Stable schema identifiers and explicit versioning.
- Positive and negative examples for published contracts.
- Compatibility policy for additive, restrictive, and breaking changes.
- Structural catalog checks in CI.

## Layout
- schemas/ — domain-grouped schema documents.
- examples/ — illustrative payloads.
- docs/SCHEMA-REGISTRY.md — governance and compatibility rules.
- tools/check_schema_catalog.py — standard-library structural checker.
- tests/ — automated catalog tests.
- .github/workflows/validate.yml — CI validation.

## Validate locally
Requires Python 3.10+; no third-party packages are needed.

    python tools/check_schema_catalog.py
    python -m unittest discover -s tests -v

## Compatibility policy
Adding an optional property is generally compatible. Removing a property, changing its type, tightening accepted values, or changing required fields is potentially breaking and requires a major-version decision plus migration notes. Unknown critical discriminators must not be silently ignored. Schema validity is not proof of truth, safety, authorization, or semantic correctness.

## Status
Scaffolded, v0.1.0. Initial common metadata schema and structural CI are present. The standard-library checker does not claim full JSON Schema semantic validation; consumers should use a conformant Draft 2020-12 validator.

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
