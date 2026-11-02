# Component Audit — agent-audit-provenance — 2026-11-02

**Repository:** [PCakes303/agent-audit-provenance](https://github.com/PCakes303/agent-audit-provenance)  
**Audited implementation commit:** `44a8b23ac6d8f641597a12a0184f900422861c8f`  
**Baseline CI:** [Run 41421033960](https://github.com/PCakes303/agent-audit-provenance/actions/runs/41421033960) — success  
**Remediation commits:** `46075af6ee412d35c07bc28cc060d486deacd407`, `fef35ad1c2b864d9b323bdbe2d30638e81f2321b`  
**Remediation CI:** [Run 41490403369](https://github.com/PCakes303/agent-audit-provenance/actions/runs/41490403369) — in progress at checkpoint creation  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental local JSONL hash-chain append/verification prototype; not a trusted audit service or immutable ledger.

## Verified implementation

- Draft 2020-12 audit-event schema defines required event identity, timestamp, actor, action, resource, outcome, details, previous hash and event hash.
- Python CLI appends JSONL records using canonical UTF-8 JSON (sorted keys, compact separators, non-ASCII preserved) and SHA-256 digest links.
- Verification checks event shape, previous-hash continuity and event digest. Append verifies the existing chain before adding a new record.
- Timestamp validation requires an ISO-8601/RFC-3339 timezone offset. Unknown fields, blank lines, malformed JSON, invalid outcomes and caller-supplied digest fields are rejected.
- Ten unit tests cover single and multiple append/verify, modified payload, broken link, missing fields, invalid outcome, caller-supplied digest fields, unknown fields, timezone requirement and blank lines.
- Starter build runs the full unit suite and an append/verify CLI smoke test. Baseline CI run 41421033960 succeeded.
- README, contract, threat model, capabilities and security policy accurately disclaim event-producer authentication, event truth, trusted timestamps, truncation resistance without external anchors, digital signatures, immutable storage and production SIEM/retention services.
- License status remains pending review; no license was added.

## Corrections committed during audit

- `46075af6ee412d35c07bc28cc060d486deacd407`: removed stale `10 / 29` portfolio-position text and added explicit pending-license disclosure to README.
- `fef35ad1c2b864d9b323bdbe2d30638e81f2321b`: clarified that a dedicated private reporting address is not published and that a private route must be configured before production use.
- Created [issue #1](https://github.com/PCakes303/agent-audit-provenance/issues/1) for schema/validator conformance, event-size limits, private reporting verification and repository settings.

## Findings and remaining exceptions

1. **Blocking schema/validator drift:** the schema limits event_id, event_type, action and resource lengths, but the hand-written validator does not enforce those maxima. Actor id/type and details have no effective size/complexity limits. The details object can contain arbitrarily large or sensitive payloads. CI does not execute the normative JSON Schema.
2. **Private reporting route unverified:** SECURITY.md now discloses that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories are enabled or configure an owner-approved private route.
3. **GitHub About metadata incomplete:** live description, homepage and topics are empty. Apply and verify actual About settings.
4. **License pending:** no root `LICENSE` file or GitHub license declaration was observed. README now states that reuse and redistribution rights must not be assumed.
5. **Staging parity outstanding:** refresh staging-to-remote path/blob-SHA parity against current `main` before portfolio-wide sign-off.
6. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
7. **Hash-chain trust limits:** the implementation does not authenticate event producers, prove event truth, prevent complete log replacement or suffix truncation without an independent checkpoint, provide trusted timestamps, encrypt records or implement signatures/WORM storage. Local filesystem access is outside its trust guarantee.

## Acceptance to clear BLOCKED

- Enforce all schema constraints, execute Draft 2020-12 validation in CI or demonstrate validator parity, and add event/actor/details size and complexity bounds.
- Verify a private vulnerability reporting route.
- Apply and verify GitHub About metadata and repository administration controls.
- Record approved licensing decisions before adding license files.
- Refresh staging parity.
- Before production use, implement authenticated ingestion, signatures and key management, independently anchored checkpoints, access control, retention/privacy governance, monitoring and independent security review.

A passing starter CI run validates the local prototype and ten tests only. It does not establish authenticity, completeness, non-repudiation, trusted time, immutable storage or production audit readiness.
