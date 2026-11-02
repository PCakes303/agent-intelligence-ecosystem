# Component Audit — agent-identity-trust — 2026-11-02

**Repository:** [PCakes303/agent-identity-trust](https://github.com/PCakes303/agent-identity-trust)  
**Baseline audited commit:** `6d53a2af501eb05bb929d5f3da07cf1dd316e6b1`  
**Baseline CI:** [Run 41407425998](https://github.com/PCakes303/agent-identity-trust/actions/runs/41407425998) — success  
**Remediation commits:** `e816ee8c2aae2deb91903c016f54dce0cfac508d`, `9ccbadf98e660a20444f2f39eaff6785b031f6b5`, `c37299b015a18c84ae13892bd3c96bc6fc6c0db8`  
**Latest CI after remediation:** [Run 41489911336](https://github.com/PCakes303/agent-identity-trust/actions/runs/41489911336) — success (validator, unit tests and starter build completed)  
**Disposition:** **BLOCKED**  
**Maturity:** Scaffolded principal identity data contract and local validator; not an identity provider or authentication/authorization service.

## Verified implementation

- Draft 2020-12 principal schema defines principal ID, principal type, issuer, creation time, optional display name, public-key fingerprint and status.
- Example principal, local Python validator, five unit tests, documentation and starter CI are present.
- The validator rejects unsupported principal types/statuses, non-HTTPS/non-SPIFFE issuers and invalid ISO timestamps.
- README explicitly says principal identifiers are not proof of authentication, authorization or human ownership; it identifies SPIFFE/SPIRE, OAuth 2.0 and OpenID Connect as integration targets, not implemented services.
- Capabilities correctly mark principal data contracts as scaffolded and delegation/revocation as planned. Manifest license status is pending review. Compatibility dependencies are declared only; no tested combinations are recorded.
- Baseline CI run 41407425998 passed. Remediation CI run 41489911336 was still in progress when this checkpoint was written.

## Remediations committed

- `e816ee8c2aae2deb91903c016f54dce0cfac508d`: replaced unrelated-account guidance in `AGENTS.md` with PCakes303 / MrCakes931 scope and an explicit boundary against unrelated repositories.
- `9ccbadf98e660a20444f2f39eaff6785b031f6b5`: removed the unrelated reporting-profile link from `SECURITY.md`; clarified that no dedicated private reporting address is published and that a private route must be configured before production use.
- `c37299b015a18c84ae13892bd3c96bc6fc6c0db8`: added README disclosure that license selection is pending and reuse/redistribution rights must not be assumed.
- Created [issue #1](https://github.com/PCakes303/agent-identity-trust/issues/1) for private reporting-channel configuration and schema/validator conformance.

## Findings and remaining exceptions

1. **Blocking private reporting gap:** no verified private vulnerability-reporting route is published/configured in the evidence available to this audit. SECURITY.md now discloses this honestly. Enable GitHub private vulnerability reporting/security advisories or publish an owner-approved private route and verify it.
2. **Blocking schema/validator drift:** the schema requires principal_id length 3–256 and rejects additional properties, while the hand-written validator only checks non-empty IDs and accepts unknown fields. Optional display_name/public_key_fingerprint type and length constraints are not enforced by the validator. The schema requires date-time; Python's current parser accepts timezone-naive ISO timestamps. Add conformant schema validation to CI or demonstrate validator parity with negative tests.
3. **License pending:** no root LICENSE file or GitHub license declaration was observed. No license was added.
4. **GitHub About metadata incomplete:** live repository metadata has no description, homepage or topics.
5. **No identity service:** no credential issuance, authentication, authorization decision service, key management, delegation implementation, revocation service or runtime integration was found. These must remain absent from claimed capabilities until implemented and tested.
6. **Compatibility not demonstrated:** foundation and schema-registry dependencies are declared; tested_combinations is empty.
7. **Administration controls unverified:** branch protection and repository security-feature settings were not confirmed through the available integration.

## Acceptance to clear BLOCKED

- Enable and verify a private vulnerability reporting route.
- Align the validator with the schema, preferably by running a Draft 2020-12 validator in CI, and add negative tests for ID bounds, unknown fields, optional property types/lengths and timezone-aware timestamps.
- Keep license pending until an explicit repository/artifact decision is approved.
- Apply and verify About metadata and repository administration controls.
- Publish reproducible cross-repository tests before marking dependencies tested.

A green starter CI run validates the current sample and five tests only. It does not prove real authentication, authorization, credential security, revocation, delegation, interoperability or production readiness.
