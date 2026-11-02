# Component Audit — agent-secure-supply-chain — 2026-11-02

**Repository:** [PCakes303/agent-secure-supply-chain](https://github.com/PCakes303/agent-secure-supply-chain)  
**Audited implementation commit:** `22f90c9290e2f85393ca451af649bc4f9a14ac1b`  
**Baseline CI:** [Run 41399364550](https://github.com/PCakes303/agent-secure-supply-chain/actions/runs/41399364550) — success  
**Remediation commits:** `6dd8bc1f1b41b262a841d2b2faeca1e8651d051f`, `04d063de9b36692bf12ce9215075165bc9eb4152`  
**Latest remediation CI:** [Run 41490619448](https://github.com/PCakes303/agent-secure-supply-chain/actions/runs/41490619448) — success (dependency-free starter build and eleven unit tests passed)  
**Disposition:** **BLOCKED**  
**Maturity:** Scaffolded supply-chain artifact metadata contract and structural validator; not a signature-verification or artifact-trust service.

## Verified implementation

- Draft 2020-12 schema describes artifact name/version/SHA-256 digest, HTTPS source repository and commit identifier, SPDX/CycloneDX SBOM reference, and signature-presence/verification flags.
- Dependency-free Python validator checks top-level and nested object shapes, SHA-256 syntax, commit syntax, HTTPS source/SBOM references and contradictory signature flags.
- Eleven unit tests cover valid records, digest algorithm/format, non-HTTPS and malformed source URLs, URL credentials, bad commit, non-HTTPS SBOM, contradictory signature state, unknown top-level field and non-object input.
- CI runs the starter build; baseline run 41399364550 succeeded after earlier URL-hardening work.
- README, contract, threat model and capability metadata correctly state that the validator does not download artifacts, generate SBOMs, verify signatures, authenticate publishers, scan dependencies or establish trust. No SLSA/in-toto conformance or production readiness is claimed.
- Manifest license status is pending review; no license was added.

## Corrections committed during audit

- `6dd8bc1f1b41b262a841d2b2faeca1e8651d051f`: removed stale `08 / 29` portfolio-position text and added explicit pending-license disclosure to README.
- `04d063de9b36692bf12ce9215075165bc9eb4152`: removed the unverified profile fallback from SECURITY.md and clarified that a private reporting route must be configured before production use.
- Created [issue #1](https://github.com/PCakes303/agent-secure-supply-chain/issues/1) for hostile URL handling, schema parity, payload bounds, private reporting and repository settings.

## Findings and remaining exceptions

1. **Blocking hostile-URL validation gap:** `sbom.uri` accepts HTTPS URLs containing embedded username/password even though `source.repository` rejects URL credentials. `urlparse` may raise `ValueError` for malformed bracketed hosts; the validator does not consistently catch parser exceptions and may crash instead of returning a validation error.
2. **Schema/validator parity and resource bounds:** the normative JSON Schema is not executed in CI. There are no explicit record-size, field-length, nesting-depth or collection bounds. The threat model already lists resource exhaustion as a residual risk.
3. **Private reporting route unverified:** SECURITY.md now discloses that a private route must be configured if GitHub private reporting is unavailable. Verify the feature is enabled or configure an owner-approved private channel.
4. **GitHub About metadata incomplete:** live description, homepage and topics are empty. Apply and verify actual About settings.
5. **License pending:** no root `LICENSE` file or GitHub license declaration was observed. README now states that reuse and redistribution rights must not be assumed.
6. **Staging parity outstanding:** refresh staging-to-remote path/blob-SHA parity against current `main` before portfolio-wide sign-off.
7. **Administration controls unverified:** branch protection/rulesets, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
8. **No supply-chain trust services:** no SBOM generation, artifact retrieval, signature verification, publisher authentication, dependency scanning, signed release or trusted provenance service is implemented.

## Acceptance to clear BLOCKED

- Reject URL userinfo consistently and convert malformed URL parser exceptions into validation errors.
- Add schema validation to CI or demonstrate validator parity, and enforce bounded document/field/nesting/collection sizes.
- Verify a private vulnerability reporting route.
- Apply and verify GitHub About metadata and repository administration controls.
- Record explicit license decisions and refresh staging parity.
- Keep all cryptographic verification, publisher identity and SLSA/in-toto claims marked unimplemented until independently tested.

A passing structural validator and unit suite do not prove artifact authenticity, SBOM correctness, signature validity, publisher identity, dependency safety or production supply-chain integrity.
