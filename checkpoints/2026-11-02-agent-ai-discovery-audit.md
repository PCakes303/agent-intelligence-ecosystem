# Component Audit — agent-ai-discovery — 2026-11-02

**Repository:** [PCakes303/agent-ai-discovery](https://github.com/PCakes303/agent-ai-discovery)  
**Audited implementation commit:** `f9aefb7edce2ae49cbaabea71c28d37c0b489814`  
**Baseline CI:** [Run 41393954047](https://github.com/PCakes303/agent-ai-discovery/actions/runs/41393954047) — success; five unit tests and starter build on Python 3.12  
**Remediation commits:** `39873ac1b30e75df3216f81556010170be2a21d8`, `bd9c5a4b85ac7091a972b91b2959676c4231f6d0`, `155c4a0c44519f7280aec50b7885c61da0ce49bb`, `f326dba4b5673008dc22b60181ec9267b74d9b69`, `07420b7da2cf11f6faa924abc6a26db7edaf7141`, `b60dd657ff7a0cac1ded9133830f10a4ccc71fec`  
**Latest CI after remediation:** [Run 41501758046](https://github.com/PCakes303/agent-ai-discovery/actions/runs/41501758046) — success; five tests and the example index build passed on Python 3.10, 3.11 and 3.12  
**Disposition:** **BLOCKED**  
**Maturity:** Scaffolded discovery document format and local deterministic index builder; no hosted endpoint, publisher authentication or authorization service.

## Verified implementation

- Draft 2020-12 discovery schema describes publisher identity/manifest URI, generation timestamp and resource entries with IDs, kinds, names, manifest URI/version, optional capabilities/tags/summary and update timestamp.
- Standard-library validator checks basic document structure, version, publisher presence, HTTP(S) absolute URIs, ISO timestamp parseability, resource kinds, required fields and duplicate resource IDs.
- CLI builds a deterministic index sorted by resource kind and ID, and rejects duplicate resource IDs across input documents.
- Five unit tests cover valid document, duplicate IDs, relative URI, unsupported kind and unknown top-level field.
- CI baseline run 41393954047 passed five tests and starter build on Python 3.12.
- Capability metadata correctly marks the document format, local index builder and input-validation behavior as scaffolded; hosted endpoint profile remains planned.
- README and contract clearly state that discovery is not identity, authorization or execution; consumers must resolve authoritative manifests, authenticate publishers and authorize actions independently.
- Compatibility metadata lists master, resource-manifest, schema-registry and identity-trust as declared-only; no tested combinations are present.
- License remains pending review; no license was added.

## Corrections committed during audit

- `39873ac1b30e75df3216f81556010170be2a21d8`: corrected README to distinguish scaffolded document/index/validation capabilities from the planned hosted endpoint.
- `bd9c5a4b85ac7091a972b91b2959676c4231f6d0`: corrected `llms.txt` capability maturity wording.
- `155c4a0c44519f7280aec50b7885c61da0ce49bb`: clarified that no dedicated private reporting address is published and added consumer-side trust/input-boundary requirements.
- `f326dba4b5673008dc22b60181ec9267b74d9b69` and `07420b7da2cf11f6faa924abc6a26db7edaf7141`: expanded push and pull-request path filters to include README/docs/security/manifest/metadata changes and added a Python 3.10–3.12 matrix.
- `b60dd657ff7a0cac1ded9133830f10a4ccc71fec`: added explicit README disclosure that licensing is pending and reuse rights must not be assumed.
- Created [issue #1](https://github.com/PCakes303/agent-ai-discovery/issues/1) for parser hardening, schema/runtime parity, metadata and governance.

## Findings and remaining exceptions

1. **Blocking hostile-input parsing gap:** CLI uses default `json.loads`, allowing duplicate keys and non-standard numeric constants. No document byte-size, nesting-depth, resource-count or string-length ceilings are enforced. Add strict parsing and resource budgets before indexing untrusted documents.
2. **Type-validation gaps:** publisher ID/name are checked only for truthiness, not string type/format. Resource `manifest_version` is not type-checked. Malformed ID or kind types can raise `TypeError` instead of controlled validation errors.
3. **URI policy incomplete:** validator accepts HTTP and HTTPS and does not reject embedded credentials or fragments. The schema uses generic URI format; decide and enforce the intended policy consistently.
4. **Timestamp semantics incomplete:** `datetime.fromisoformat` accepts timezone-naive timestamps; contract/schema expect date-time semantics. Require timezone-aware RFC3339 values.
5. **Array/field bounds incomplete:** capabilities/tags are not uniqueness-checked or bounded by item count/string length. Publisher/resource names, manifest versions and other strings have no explicit size ceilings.
6. **Schema/runtime parity absent:** CI does not execute the normative Draft 2020-12 schema; README correctly disclaims full schema validation. Add a standards-compliant validation step or a comprehensive parity suite.
7. **Private reporting route unverified:** SECURITY.md now states no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private route.
8. **GitHub About metadata incomplete:** description, homepage and topics are empty. Apply and verify actual About settings.
9. **License pending:** no root LICENSE file or GitHub license declaration was observed. README now explicitly records pending status.
10. **Staging evidence unavailable:** no `STAGING-STATUS.md` or master staging packet was found. Do not claim staging parity.
11. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed.
12. **No hosted discovery/trust integration:** publisher authentication, authorization, endpoint hosting and cross-repository runtime compatibility are not implemented. Dependencies remain declared-only.

## Acceptance to clear BLOCKED

- Add strict duplicate-key/nonstandard-number rejection and document byte/depth/resource/field bounds.
- Validate types and formats for every field; reject malformed input with controlled errors.
- Decide and enforce URI and timezone-aware timestamp policy consistently across schema and validator.
- Add schema validation and positive/negative/boundary parity tests.
- Verify private reporting, About metadata and repository administration settings.
- Keep licensing pending until explicitly approved; create a staging packet only if a retained source copy is required.
- Keep hosted endpoint, publisher authentication and interoperability marked planned until implemented and tested.

Passing the five-test baseline validates the current small local fixture only. It does not establish full schema conformance, publisher identity, freshness enforcement, authorization, or production discovery service readiness.
