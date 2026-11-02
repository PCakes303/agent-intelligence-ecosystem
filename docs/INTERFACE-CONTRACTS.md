# Interface and Contract Engineering

## Contract types

Every cross-repository dependency must identify the contract being consumed: versioned schema, API, protocol, event, library API, CLI contract, or specification. A dependency on a repository name alone is insufficient for production integration.

## Required contract metadata

- Stable contract identifier and semantic version.
- Normative schema/specification and canonical examples.
- Producer and consumer repository IDs.
- Compatibility policy and deprecation window.
- Positive, negative, malformed, boundary, and security test vectors.
- Version negotiation and unsupported-version behavior.
- Provenance for generated code and published artifacts.

## Compatibility policy

Use semantic versioning where the interface supports it. Breaking changes require a major version or a separately versioned contract, migration guidance, and explicit consumer impact review. Additive changes still require compatibility tests; they are not automatically safe for every schema or protocol.

## Consumer-driven verification

Consumers publish executable contract tests or fixtures. Producers run them before release. The conformance lab later aggregates these tests but does not replace repository-local CI.

## No implicit trust

A schema-valid message is not necessarily authorized or safe. Validate identity, authorization, size/resource limits, replay protection, and content-specific constraints separately.
