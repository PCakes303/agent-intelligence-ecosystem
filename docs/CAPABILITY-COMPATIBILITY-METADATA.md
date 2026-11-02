# Capability and Compatibility Metadata Contract

**Contract version:** 1.1.0  
**Authority:** This document defines the public metadata shape consumed by the master repository's validation workflow.

## Purpose

Every existing public component repository publishes two machine-readable files at its root:

- `capabilities.json` describes what the repository actually provides, with maturity and evidence.
- `compatibility.json` describes declared dependency relationships separately from verified interoperability.

The master registry remains authoritative for repository identity, existence, visibility, maturity, and dependency graph. These component files describe local capability claims; they do not override the master registry.

## Capability status

| Status | Meaning |
|---|---|
| `planned` | Intended work; not implemented. Evidence may be empty. |
| `scaffolded` | A contract, schema, example, validator, tests, or other initial artifact exists. |
| `implemented` | The named behavior is implemented; cite the implementation path. |
| `tested` | The behavior has repeatable test evidence; cite the test and successful CI/run evidence. |
| `released` | A versioned release artifact exists; cite its release/tag and provenance. |

Do not use repository-wide maturity as a substitute for capability-level status. A repository can be scaffolded while some capabilities remain planned. Avoid calling a capability tested merely because a test file exists.

Every non-planned capability must include one or more evidence paths. Status is a claim about the named capability only, not a security certification or production-readiness guarantee. Include limitations where the claim could be misunderstood.

## Compatibility status

Each dependency uses one of:

- `declared`: architectural or contract dependency; no interoperability test is claimed.
- `tested`: a reproducible compatibility test has been run and evidence is published.
- `unsupported`: the combination is explicitly not supported.

A `tested` dependency must include evidence. Cross-repository tested combinations must identify all participating repositories, pass/fail result, and evidence locations. An empty `tested_combinations` array means no cross-repository combinations are currently asserted as tested.

A declared dependency is not proof that the dependency repository exists, is installed, or interoperates at runtime. The master registry validates repository identity and graph membership separately.

## Schemas and validation

- [Capability schema](../schemas/capabilities.schema.json)
- [Compatibility schema](../schemas/compatibility.schema.json)
- [Validator](../tools/validate_capability_metadata.py)
- [Regression tests](../tests/test_capability_metadata.py)

The master starter build fetches the public metadata files for each existing public component repository listed in the canonical registry and validates their structure and evidence discipline. Planned repositories are not fetched and must not advertise live files or endpoints.

## Licensing and public data

License declarations must match a committed LICENSE file and a recorded decision. Until verified, use a pending-review state and do not claim a specific license in README text. Public metadata must not contain private operational details, secrets, internal endpoints, or personal information.

## Current baseline

All 20 existing public component repositories publish capability and compatibility metadata using contract version 1.1.0, and the master starter-build validator has passed against the live remote metadata. Their compatibility relationships remain declared, not tested, unless an individual tested combination and evidence are explicitly listed. Capability statuses are deliberately conservative: existing contracts and tools are described as scaffolded, while incomplete or unimplemented items remain planned. No A2A deployment or production MCP service is implied by these files.
