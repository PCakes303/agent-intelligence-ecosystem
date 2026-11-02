# Component Audit — agent-capability-registry — 2026-11-02

**Repository:** [PCakes303/agent-capability-registry](https://github.com/PCakes303/agent-capability-registry)  
**Audited baseline:** `0220f7ecc89589b9ccd256a705188d7ff27d1371`  
**Baseline CI:** [Run 41413613566](https://github.com/PCakes303/agent-capability-registry/actions/runs/41413613566) — success  
**Remediation commits:** `c6128b2741695529cf034764a1d5c97af0838b25`, `0f8f3e6ecce38f8e40fff37107ab002810689075`, `4f238bfa89963008e01700ed78430fc2eeb56361`, `4e9dffd1cfcf5dcbacbd3a7ae6773dfff7cfcf0f`, `4486f5ac465de3f2746eaea45b41cc679c2ece0e`, `1c052989e0bcdfe50389e7b6b4a8e3679fac366f`, `6fc7c9a89503fc7f843a53bddc616ef4360a11aa`, `fc49cc3b4f20c9ac6d2b02a78f48bcf69200e9de`, `c7dec4d551b0578e2b9f4500d0fc81062e928562`, `85d8a70783c6ea6673c2a8a8907db01e93ec9345`  
**Final remediation CI:** [Run 41493172965](https://github.com/PCakes303/agent-capability-registry/actions/runs/41493172965) — success on Python 3.10, 3.11 and 3.12; 11 tests per matrix job  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental bounded process-local capability catalog and advisory matcher; not an identity, authorization, attestation or execution service.

## Verified implementation

- Capability and requirement models validate bounded identifiers, descriptions, numeric semantic versions, and bounded string-to-string attribute mappings.
- Registry capacity is bounded (default 10,000). Matching now caps requirements at 128 by default and iterates the incoming iterable incrementally, avoiding an unbounded `list(requirements)` materialization.
- Registered declarations are copied into immutable attribute mappings, so later mutation of the caller's source dictionary or returned capability object cannot mutate indexed state.
- Requirement attributes are also snapshotted for a stable match operation.
- The policy callback must return explicit boolean `True`; false, non-boolean and raising callback results deny the candidate.
- Matching requires all requested capabilities to be satisfied by the same agent and returns deterministic sorted results.
- CI run 41493172965 passed on Python 3.10, 3.11 and 3.12; each job ran 11 unit tests.
- Capability metadata, README, contract, threat model, security policy, agent instructions and staging status now describe immutability and bounded matching.
- License remains pending review; no license was added. Dependencies remain declared, not tested combinations.

## Corrections committed during audit

- `c6128b2741695529cf034764a1d5c97af0838b25`: model attribute contracts now accept read-only mapping snapshots.
- `0f8f3e6ecce38f8e40fff37107ab002810689075`: registry snapshots and freezes registered attributes, bounds match requests, and rejects truthy non-boolean policy results.
- `4f238bfa89963008e01700ed78430fc2eeb56361`: added tests for source mutation, immutable returned attributes, requirement-count limits and non-boolean policy results.
- `4e9dffd1cfcf5dcbacbd3a7ae6773dfff7cfcf0f`: documented immutable declarations and bounded requirement matching in README.
- `4486f5ac465de3f2746eaea45b41cc679c2ece0e`: clarified private-reporting gap and trust boundaries in SECURITY.md.
- `1c052989e0bcdfe50389e7b6b4a8e3679fac366f` and `6fc7c9a89503fc7f843a53bddc616ef4360a11aa`: documented matching limits and updated threat model.
- `fc49cc3b4f20c9ac6d2b02a78f48bcf69200e9de`: reconciled deployment/audit status.
- `c7dec4d551b0578e2b9f4500d0fc81062e928562`: aligned capability metadata with immutable bounded matching.
- `85d8a70783c6ea6673c2a8a8907db01e93ec9345`: strengthened agent instructions.
- Created [issue #1](https://github.com/PCakes303/agent-capability-registry/issues/1) for schema binding, authenticated policy integration, attestations and governance.

## Findings and remaining exceptions

1. **No authenticated agent identity:** agent IDs are declaration strings; no trusted Identity & Trust integration or authenticated principal context exists.
2. **No production authorization:** the decision callback is an integration seam, not a policy service or protected-resource enforcement point.
3. **No capability attestation:** declarations are untrusted claims. There is no signature profile, signed publisher identity, evidence verification, key lifecycle or proof that a capability works.
4. **Schema parity not enforced:** a JSON Schema exists, but the Python models do not execute the normative Draft 2020-12 schema in CI. Add parity tests for valid/invalid and boundary cases.
5. **No cross-repository integration:** Resource Manifest, Schema Registry and Policy Engine dependencies are declared but not pinned or tested in reproducible combinations.
6. **No distributed/network service:** registry is process-local; there is no authenticated discovery API, replication, durable storage or consistency model.
7. **Private reporting route unverified:** SECURITY.md states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private channel.
8. **GitHub About metadata incomplete:** description exists; homepage and topics are empty. Apply and verify actual About settings.
9. **License pending:** no root LICENSE file or GitHub license declaration was observed; reuse and redistribution rights must not be assumed.
10. **Staging parity outstanding:** refresh staging-to-remote path/blob-SHA parity against current `main` before portfolio sign-off.
11. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.

## Acceptance to clear BLOCKED

- Execute canonical Draft 2020-12 schema validation in CI and demonstrate model/schema parity.
- Integrate authenticated agent identity and a versioned policy-engine decision service with fail-closed resource enforcement.
- Add signed capability attestations, publisher identity/key lifecycle and evidence validation before treating declarations as trusted.
- Pin and test Resource Manifest, Schema Registry and Policy Engine combinations.
- Define authenticated distributed discovery only after abuse controls, audit, rate limits and consistency semantics exist.
- Verify private reporting, About metadata, repository settings, staging parity and licensing decision.

Passing the 11-test suite on three Python versions validates only the local bounded matcher. It does not establish identity, authorization, capability truth, security attestation, distributed consistency or production readiness.
