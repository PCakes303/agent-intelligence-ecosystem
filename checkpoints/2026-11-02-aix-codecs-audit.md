# Component Audit — aix-codecs — 2026-11-02

**Repository:** [PCakes303/aix-codecs](https://github.com/PCakes303/aix-codecs)  
**Audited implementation commit:** `9edce84c0f00db0fbe2d8ddfa302510329e66503`  
**Baseline CI:** [Run 41427817571](https://github.com/PCakes303/aix-codecs/actions/runs/41427817571) — success  
**Remediation commits:** `ab013bfcc2f7f7184f9331618841b2ca09a3be7b`, `fe48c296b26fb67fbb5b0dfb6bd5e820d96e6bf5`, `220226f97698de1e60fb210d3b766c0d22e05cc5`  
**Latest remediation CI:** [Run 41491180433](https://github.com/PCakes303/aix-codecs/actions/runs/41491180433) — success (eight unit tests on Python 3.10, 3.11 and 3.12)  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental Python RFC 8785 canonical JSON encoder and strict JSON decoder; no cross-language conformance or production ingress boundary.

## Verified implementation

- Uses pinned `rfc8785==0.1.4` rather than ordinary sorted JSON serialization.
- Encoder returns canonical UTF-8 bytes and wraps unsupported-value/canonicalization errors in `CodecError`.
- Decoder accepts bytes or strings, strictly decodes UTF-8, rejects malformed JSON, duplicate object keys and non-standard numeric constants, and optionally requires byte-for-byte RFC 8785 canonical form.
- Eight unit tests cover key ordering/whitespace normalization, round trip, canonical/noncanonical strict mode, duplicate keys, NaN, invalid UTF-8 and non-JSON Python values.
- CI tests Python 3.10, 3.11 and 3.12; baseline run 41427817571 succeeded.
- Contract correctly requires RFC 8785 and explicitly delegates hostile-input payload-size, nesting-depth, resource-budget, replay and schema checks to transport-facing integrations.
- README, SECURITY.md and capability metadata explicitly disclaim authentication, authorization, transport, signatures, schema validation and cross-language conformance.
- License remains pending review; no license was added. AIX Core and Schema Registry dependencies remain declared, not tested combinations.

## Corrections committed during audit

- `ab013bfcc2f7f7184f9331618841b2ca09a3be7b`: removed obsolete `12 / 29` portfolio-position text from README.
- `fe48c296b26fb67fbb5b0dfb6bd5e820d96e6bf5`: clarified the absence of a published private reporting address and documented caller-side trust/resource limits in SECURITY.md.
- `220226f97698de1e60fb210d3b766c0d22e05cc5`: reconciled staging status, distinguished historical deployment evidence from current parity, and recorded metadata/private-reporting follow-ups.
- Created [issue #1](https://github.com/PCakes303/aix-codecs/issues/1) for expanded RFC vectors, bounded ingress integration, private reporting, metadata and staging verification.

## Master catalog reconciliation

The first master registry maturity update exposed a catalog drift: `registry/public-agent-catalog.json` retained the previous AIX Codecs status. Master regression run 41491355197 correctly failed `test_catalog_matches_public_registry`. The catalog entry was synchronized in commit `ac982e59efe5076af81b5c29d11f83993405d2df`; master validation run [41491483004](https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41491483004) then passed registry validation, resource-manifest validation, policy smoke test, all 47 regression tests and entry-level build.

## Post-audit README back-check — 2026-11-02

A second live-file inspection found that the earlier commit titled as removing the obsolete 12 / 29 portfolio-position line had not actually removed it from the current README. The line has now been removed and explicit pending-license disclosure added in commit 1f16c60df3089239245b82cbae6374b04f1a9b29. The live README was re-fetched and confirmed to contain neither the obsolete portfolio-position line nor a missing license-status disclosure. [CI run 41503562843](https://github.com/PCakes303/aix-codecs/actions/runs/41503562843) completed successfully; the eight-test Python 3.10–3.12 matrix remains green.

## Findings and remaining exceptions

1. **Conformance coverage incomplete:** eight tests do not yet demonstrate the full RFC 8785 edge-case set promised by the contract. Add shared vectors for Unicode/surrogates, numeric serialization edge cases, negative zero, exponent formatting, arrays and nested values.
2. **No cross-language evidence:** only a Python implementation exists. Cross-language compatibility remains planned; do not claim conformance until an independent implementation passes shared vectors.
3. **Resource limits are caller responsibility:** the decoder has no payload-byte-size or explicit nesting-depth budget. This is documented; every transport-facing integration must enforce hard limits before decode and apply schema validation.
4. **Private reporting route unverified:** SECURITY.md states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private channel.
5. **GitHub About metadata incomplete:** description exists; homepage and topics are empty. Apply and verify actual About settings.
6. **License pending:** no root LICENSE file or GitHub license declaration was observed. Reuse and redistribution rights must not be assumed.
7. **Staging parity outstanding:** refresh staging-to-remote path/blob-SHA parity against current `main` before portfolio-wide sign-off.
8. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.

## Acceptance to clear BLOCKED

- Add complete RFC 8785 positive/negative vectors and fuzz/property coverage.
- Add an independent implementation and byte-identical cross-language conformance suite before claiming interoperability.
- Enforce payload-size, nesting-depth and resource budgets in every untrusted-input integration before decode.
- Verify private vulnerability reporting, About metadata and repository administration controls.
- Record an explicit repository/artifact license decision and refresh staging parity.

A passing CI matrix confirms the eight current Python tests on three Python versions. It does not establish full RFC conformance, cross-language interoperability, safe hostile-input ingestion, authentication, authorization or production readiness.
