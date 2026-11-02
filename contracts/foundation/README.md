# Foundation and cybersecurity contract baseline

**Status:** proposed ecosystem contract, version 1.0.0  
**Applies to:** repositories 01–07 and every downstream ecosystem component  
**Normative language:** MUST, MUST NOT, SHOULD, MAY are used as requirements terms.

This contract is the common security and engineering floor. Individual repositories may strengthen it. They MUST NOT silently weaken it. A deviation requires an Architecture Decision Record (ADR), an explicit risk owner, compensating controls, and a review date.

## Design principles

1. **Explicit trust boundaries.** Treat each agent, tool, service, node, repository, dataset, and operator domain as a distinct principal until authenticated and authorized otherwise.
2. **Deny by default.** No identity, capability, tool, network route, filesystem path, or data operation is allowed merely because it is discoverable.
3. **Least authority.** Grant the smallest action set, resource scope, and duration needed for a task. Prefer short-lived, revocable credentials.
4. **Authenticated provenance.** Record who or what performed an action, under which identity and policy decision, against which resource and version.
5. **Fail closed for security decisions.** If identity, policy, revocation, or required integrity checks cannot be established, protected operations MUST be denied. Availability fallbacks must not silently bypass authorization.
6. **Interoperability by composition.** Reuse established protocols and standards; do not replace MCP, A2A, OAuth/OIDC, SPIFFE, OPA, Sigstore, SLSA, or OpenTelemetry without a documented gap and ADR.
7. **Data minimization.** Exchange references and scoped claims rather than copying sensitive context by default. Do not transmit private model reasoning or hidden chain-of-thought.
8. **Observable but privacy-aware.** Audit security-relevant events while minimizing secrets, personal data, and unnecessary payload capture.

## Shared contract

Every implementation claiming conformance MUST:

- identify its principals and trust domains;
- authenticate callers using a documented mechanism appropriate to the deployment;
- authorize every protected operation at the resource/action boundary;
- validate untrusted inputs against versioned schemas;
- bind actions to an explicit policy decision and capability scope;
- support credential expiry and revocation;
- emit structured audit events for security-relevant actions and decisions;
- protect integrity and provenance of released artifacts;
- document data classification, retention, and deletion behavior;
- test denial paths, malformed inputs, replay/idempotency behavior, and failure modes.

## Repository responsibilities

| ID | Repository | Owns | Must consume |
|---|---|---|---|
| FND-01 | agent-foundation-spec | Architecture vocabulary, lifecycle, normative baseline, compatibility rules | Master registry |
| FND-02 | agent-resource-manifest | Resource identity and descriptive metadata | FND-01, FND-03, FND-04 |
| FND-03 | agent-schema-registry | Schema publication, versioning, compatibility and validation | FND-01 |
| FND-04 | agent-identity-trust | Principal identity, authentication, trust domains, credential lifecycle and revocation | FND-01, FND-06 |
| FND-05 | agent-secure-supply-chain | SBOM, dependency controls, build provenance, signing and release verification | FND-01, FND-04, FND-07 |
| FND-06 | agent-policy-engine | Authorization model, policy evaluation, decision contract and enforcement guidance | FND-01 |
| FND-07 | agent-audit-provenance | Event model, provenance references, integrity protection and audit verification | FND-01, FND-03, FND-04 |

## Contract boundaries

- A manifest describes a resource; it does not grant permission to use it.
- Discovery returns candidates; it does not establish trust or authorize execution.
- Authentication establishes a principal or workload identity; it does not imply authorization.
- Policy evaluation returns a decision for a specific principal, action, resource, context and policy version; enforcement remains at the protected boundary.
- An audit hash chain detects modification relative to a trusted checkpoint; a hash alone does not prove that an event is true, complete, or independently witnessed.
- An SBOM describes declared software components; it does not prove that a build used those components unless bound to verifiable build provenance.
- A signature proves control of a signing key for signed bytes; it does not prove the publisher is trustworthy or the content is safe.

## Compatibility and change control

A change is breaking when it removes or renames a required field, changes field meaning, weakens a security guarantee, changes default authorization behavior, or invalidates a previously conforming interaction. Breaking changes require a major contract version and migration guidance. Additive optional fields generally require a minor version. Editorial corrections may use a patch version.

Every change MUST include: requirement IDs affected, compatibility classification, migration path, test evidence, and an ADR when security posture or architecture changes.

## Implementation status

This file is a proposed shared contract in the master repository. It does not mean repositories 01–07 have been created or implemented. The registry remains authoritative for repository status.
