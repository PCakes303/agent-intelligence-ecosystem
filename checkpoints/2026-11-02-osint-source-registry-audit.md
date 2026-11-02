# Component Audit — osint-source-registry — 2026-11-02

**Repository:** [PCakes303/osint-source-registry](https://github.com/PCakes303/osint-source-registry)  
**Audited baseline:** `745aab1a853931bac520d5dc0dfaa129bd422ccc`  
**Baseline CI:** [Run 41428118849](https://github.com/PCakes303/osint-source-registry/actions/runs/41428118849) — success  
**Remediation commits:** `a284652c7fe6201cc4f62ccaff88e335ac956be7`, `ea0003f64e4b71e11ecc9265e7d6d10dfee8479a`, `27c8ae3fa46c3e939e93ac57a43de91db20fcbaf`, `701f4cb1db90d2e7f532fefacd43265c4f427052`, `9cb2a0c799abba3e42b58d2d9057f6ae14b3134b`, `fc702a3ff109f3e2b17812c8ecfe08394f9151d1`, `0c3ec5bd4b2635cb6a5eaba27ec0f685566405f6`, `03073dd74b89c331502ab9a2b24a3ba1f36820c3`, `f1ac18405664f46a26851a54017d4d64a8f22c08`, `6c00a082d4ee0c1bbe64ff08f7eb9fa2df1de944`, `0414b139c3cf5c1af6ae672c49f887b342b4c6a5`, `8fe01f0edde2170eb27aa10cf36a930802f8dd27`, `b9781bcbe64b1ac6f78948b46a4943e5a2ce5290`, `70040b7c76c9b42e1c1108e19bc45c61b112e064`  
**Final remediation CI:** [Run 41495728166](https://github.com/PCakes303/osint-source-registry/actions/runs/41495728166) — success on Python 3.10, 3.11 and 3.12; 29 tests per matrix job; approved synthetic fixture validator passed  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental review-gated source metadata catalog; not a collector, source authenticator or legal approval service.

## Verified implementation

- Source records validate required/allowed fields, source type, access/auth modes, sensitivity, robots policy, review state, HTTPS URL syntax, terms/license metadata, purpose labels, rate limits, retention and timezone-aware review timestamps.
- Approved records require terms URL, non-empty license expression, at least one permitted purpose, review timestamp and future expiry. Expired/pending/suspended/rejected/retired sources are excluded from approved-source queries.
- URL parsing now validates port syntax and rejects malformed/out-of-range ports, credentials, whitespace and non-HTTPS URLs. This remains syntax validation only; no DNS/HTTP requests occur.
- Python array bounds now align with schema: collection constraints 3–500 characters; permitted/prohibited purpose items 2–100 characters; at most 20 entries each.
- Validation/query clocks reject non-datetime values and naive timestamps without unexpected exceptions.
- Registry capacity is hard-capped at 100,000; add/get/query/length operations are synchronized within one process.
- Registry insertion snapshots records through `SourceRecord.from_dict`, converting caller-owned mutable lists to immutable tuples before storing.
- CI run 41495728166 passed on Python 3.10, 3.11 and 3.12; each job ran 29 tests and the approved synthetic source schema CLI validation passed.
- README and metadata clearly state synthetic examples only, no real source is pre-approved, and the repository does not collect/crawl/download/query/enrich/redistribute source content.
- License remains pending review; no license was added. Resource Manifest, Schema Registry and Audit Provenance dependencies remain declared, not tested combinations.

## Corrections committed during audit

- `a284652c7fe6201cc4f62ccaff88e335ac956be7`: validate URL port syntax, align purpose/collection bounds and harden validation clock type handling.
- `ea0003f64e4b71e11ecc9265e7d6d10dfee8479a`: add hard registry capacity ceiling and synchronized operations.
- `27c8ae3fa46c3e939e93ac57a43de91db20fcbaf`, `701f4cb1db90d2e7f532fefacd43265c4f427052`, `9cb2a0c799abba3e42b58d2d9057f6ae14b3134b`, `fc702a3ff109f3e2b17812c8ecfe08394f9151d1`, `0c3ec5bd4b2635cb6a5eaba27ec0f685566405f6`, `03073dd74b89c331502ab9a2b24a3ba1f36820c3`: tests for URL ports, schema bounds, invalid clocks, capacity, concurrency, immutable snapshots and collection constraint lengths.
- `f1ac18405664f46a26851a54017d4d64a8f22c08`: removed obsolete `19 / 29` portfolio position.
- `6c00a082d4ee0c1bbe64ff08f7eb9fa2df1de944`: clarified private-reporting gap, URL syntax limitations and immutable snapshots in SECURITY.md.
- `0414b139c3cf5c1af6ae672c49f887b342b4c6a5`, `8fe01f0edde2170eb27aa10cf36a930802f8dd27`, `b9781bcbe64b1ac6f78948b46a4943e5a2ce5290`: aligned contract, threat model and capability metadata.
- `70040b7c76c9b42e1c1108e19bc45c61b112e064`: recorded audit remediation and remaining gates in staging status.
- Created [issue #1](https://github.com/PCakes303/osint-source-registry/issues/1) for authenticated approvals, schema parity and governance.

## Findings and remaining exceptions

1. **No authenticated reviewer approval:** review status, reviewer timestamp and license/terms claims are unsigned local metadata. No authenticated reviewer identity, approval signature or audit-provenance binding exists.
2. **Schema parity incomplete:** CI executes the schema CLI on the approved synthetic fixture and tests schema/model parity for that fixture, but it does not run full valid/invalid/boundary parity across all model cases.
3. **No legal determination:** a non-empty license expression and terms URL are metadata, not proof that access or a proposed use is lawful or permitted. Current terms/licensing require human review.
4. **No source authenticity/accuracy:** URL syntax and operator names do not verify host ownership, publisher identity, source accuracy, freshness or content integrity.
5. **No collection client:** no crawling, scraping, download, API access, DNS resolution, redirects or source content retrieval is implemented. This boundary must remain until a separate reviewed collector design exists.
6. **Future collector SSRF risk:** future network integrations must defend DNS rebinding, redirects, private/link-local addresses, proxy behavior, credentials, rate limits and content-type/size constraints.
7. **Private reporting route unverified:** SECURITY.md states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private channel.
8. **GitHub About metadata incomplete:** description exists; homepage and topics are empty. Apply and verify actual About settings.
9. **License pending:** no root LICENSE file or GitHub license declaration was observed; reuse and redistribution rights must not be assumed.
10. **Staging parity outstanding:** refresh staging-to-remote path/blob-SHA parity against current `main` before portfolio sign-off.
11. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.

## Acceptance to clear BLOCKED

- Run schema/model parity for the full synthetic valid/invalid/boundary suite in CI.
- Bind approvals to authenticated reviewer identity, review evidence and immutable Audit & Provenance events.
- Keep source permission, licensing, privacy and jurisdiction decisions human-reviewed and evidence-backed; do not infer legality from metadata.
- Maintain no-network collection boundary until a separate SSRF, authentication, policy, rate-limit, privacy and retention design is approved.
- Verify private reporting, About metadata, repository administration settings, staging parity and licensing decision.

Passing the 29-test suite and synthetic schema validation validates the local metadata catalog only. It does not establish legal permission, source authenticity, reviewer identity, source accuracy, lawful access or collection authorization.
