# Component Audit — aix-core — 2026-11-02

**Repository:** [PCakes303/aix-core](https://github.com/PCakes303/aix-core)  
**Audited implementation commit:** `11dc24b14382d2f019e6a6a3ad00d325018a8604`  
**Baseline CI:** [Run 41421093275](https://github.com/PCakes303/aix-core/actions/runs/41421093275) — success  
**Remediation commits:** `dae1464c6b4f05d7d3477b0c87a32f0e72c3f5d5`, `7a322fdca794750159d6fd97c49f96bf0af52938`, `4988d08c2fc9556d64ab90527e5cb0631aeec14d`  
**Latest remediation CI:** [Run 41490856354](https://github.com/PCakes303/aix-core/actions/runs/41490856354) — in progress at checkpoint creation  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental AIX semantic specification and schema-validation scaffold; no production runtime or protocol conformance certification.

## Verified implementation

- Draft 2020-12 schema defines an experimental message envelope with version, message ID, timestamp, sender, message type, task, security and provenance fields; recipient and extension areas are optional.
- CLI validates the example envelope with `Draft202012Validator` and a date/time/URI format checker.
- Eight tests cover valid fixture, missing security object, unknown top-level field, unknown message type, invalid task state, optional idempotency key, CLI acceptance and CLI rejection.
- Starter build runs the unit suite and CLI validation. Baseline CI run 41421093275 succeeded.
- Specification defines task lifecycle, context/evidence references, security context and provenance. Mapping guide treats MCP, A2A, HTTP/OpenAPI and JSON-RPC as complementary standards/transports.
- README and capability metadata explicitly state that AIX is an extension layer, not a replacement, and that no production transport, SDK/runtime, cryptographic signing, authentication, authorization enforcement or standards certification is provided.
- License remains pending review; no license was added. All declared dependencies remain untested contract relationships.

## Corrections committed during audit

- `dae1464c6b4f05d7d3477b0c87a32f0e72c3f5d5`: removed stale `11 / 29` portfolio-position text and added explicit pending-license disclosure to README.
- `7a322fdca794750159d6fd97c49f96bf0af52938`: clarified that no dedicated private reporting address is published and a private route must be configured before production use.
- `4988d08c2fc9556d64ab90527e5cb0631aeec14d`: clarified historical deployment evidence and outstanding staging parity in `STAGING-STATUS.md`.
- Created [issue #1](https://github.com/PCakes303/aix-core/issues/1) for schema bounds, private reporting and repository governance.

## Findings and remaining exceptions

1. **Blocking message complexity limits:** the schema has some string limits but does not comprehensively bound arrays and nested payloads. `capability_requirements`, `context_refs`, `evidence_refs`, `requested_scopes`, task `input_refs`, `constraints` and `extensions` can grow without explicit item/property/depth/size ceilings. Some nested identifiers also lack maximum lengths. Add bounded limits and receiver-side size/depth enforcement.
2. **Private reporting route unverified:** SECURITY.md discloses that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private route.
3. **GitHub About metadata incomplete:** live description, homepage and topics are empty. Apply and verify actual About settings.
4. **License pending:** no root `LICENSE` file or GitHub license declaration was observed. README now states reuse and redistribution rights must not be assumed.
5. **Staging parity outstanding:** historical deployment file count and CI link are preserved as history, not current byte-parity evidence. Refresh staging-to-remote blob-SHA parity.
6. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
7. **No runtime security or protocol mapping:** schema validity does not authenticate sender, authorize action, verify references, prevent replay, enforce idempotency, or ensure transport integrity/confidentiality. Concrete MCP/A2A mapping profiles and conformance tests are planned, not implemented.

## Acceptance to clear BLOCKED

- Add comprehensive bounded lengths, array/property limits, extension rules and receiver-side message size/depth limits with negative tests.
- Verify a private vulnerability reporting route.
- Apply and verify About metadata and repository administration settings.
- Record explicit licensing decisions and refresh staging parity.
- Implement concrete versioned mapping profiles and cross-implementation conformance tests before claiming interoperability.

Passing CI validates the current envelope schema and eight tests. It does not establish authentication, authorization, replay protection, delivery guarantees, interoperability or production readiness.
