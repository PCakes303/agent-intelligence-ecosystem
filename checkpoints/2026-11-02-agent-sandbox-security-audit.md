# Component Audit — agent-sandbox-security — 2026-11-02

**Repository:** [PCakes303/agent-sandbox-security](https://github.com/PCakes303/agent-sandbox-security)  
**Audited implementation commit:** `29235a9477dafdf23ced98389c952a31fc22df3d`  
**Baseline CI:** [Run 41437856656](https://github.com/PCakes303/agent-sandbox-security/actions/runs/41437856656) — success; 14 tests on Python 3.10, 3.11 and 3.12  
**Remediation commit:** `c98a6883ea08fbcbdf5cd5a6ed445a05970a6af0`  
**Remediation CI:** [Run 41499814802](https://github.com/PCakes303/agent-sandbox-security/actions/runs/41499814802) — success  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental sandbox admission policy contract and fail-closed reference validator; it never executes workloads and provides no OS isolation.

## Verified implementation

- Strict top-level and nested policy shapes are checked; unknown/missing keys are rejected.
- Numeric resource ceilings are bounded for CPU, memory, wall time, process count and output bytes; booleans are not accepted as integers.
- Filesystem declarations require read-only root, absolute POSIX paths, no NULs, no traversal components and no duplicate paths. Network intent requires default-deny and unique bounded-length egress strings.
- Execution policy requires identity, policy, stop-state and artifact-verification prerequisites and explicitly forbids enabling execution in this reference release.
- Admission evaluator requires literal boolean evidence for authenticated identity, policy allow, artifact verification, revocation clear, valid/inactive stop state and backend enforcement; it still unconditionally returns deny even when all checks pass.
- Fourteen unit tests cover valid policy, duplicate JSON keys, extra fields, bool-vs-int, numeric ceilings, path traversal, read-only root, default-deny network, disabled execution, missing/active stop state, missing backend and non-boolean evidence.
- CI passes on Python 3.10, 3.11 and 3.12 in baseline run 41437856656.
- README, contract, threat model and capabilities correctly state that no OS/container/namespace enforcement, workload execution, filesystem/network enforcement, identity/policy/revocation/emergency-control runtime, artifact verification service or compliance certification exists.
- License remains pending review; no license was added.

## Corrections and parity work

- `c98a6883ea08fbcbdf5cd5a6ed445a05970a6af0`: clarified that no dedicated private reporting address is published and that an approved private route must be configured if GitHub private reporting is unavailable; reinforced the non-execution boundary.
- Updated the retained master staging packet's `SECURITY.md` to match the audited remote policy: master commit `008b062e15e813c75a9ecd7465a342cd615511d1`.
- Recomputed Git blob parity after synchronization: **14 staged product files vs 14 remote files; zero missing, extra or differing blobs**. `STAGING-STATUS.md` is intentionally master-side deployment evidence, not a product file.
- Created [issue #1](https://github.com/PCakes303/agent-sandbox-security/issues/1) for bounded hostile-input parsing, schema parity, private reporting and metadata/settings verification.

## Post-audit parser, collection and schema hardening — 2026-11-02

The earlier blocking parser and collection findings are now remediated in the reference validator:

- e0aad6b37457e52331666b2ef334b0ba29fa6fbf: enforce a 1 MiB UTF-8 input ceiling and 32-level JSON nesting bound before json.loads; normalize malformed/deep parser failures into PolicyError; cap filesystem path arrays and egress allowlists at 64 entries; cap path strings at 1,024 and egress strings at 255 characters; reject whitespace/NUL egress values.
- d635ab1c9a5f19f3aad75c22a9cf1d20bbe227da: correct escape handling in the pre-parse JSON depth scanner.
- 9eda8a9073f251ffcad8d5cac34cc16a8e20712 and 820d4b202d3539354d0960c6a5238132b0c4fb66: add parser, size, depth, path/egress collection and schema parity tests.
- 4a3a65785c193702ebfcc031f0db0d666461d9c8 and 23b069a7a1fc5c62449dcf0f1260692f8aac18f1: align the Draft 2020-12 schema with runtime numeric bounds, path traversal/NUL rules, read-only root and execution-disabled invariants.
- 0f5179a659f5af4479131a0c295bc79da4ffdeb9: align profile ID validation with schema.
- 1ea85fb4b606ed29c2578abf3cabbce890aa147c and 1ba84a96c3a1d71aa40dc448d8dbe1351f6a27ab: add pinned jsonschema development dependency and execute schema tests in CI.
- 614c1f61570acfae296ea35c1af90977e62ea6de: correct the escaped-string regression fixture after the first run revealed it used a profile ID invalid under the new identifier contract.
- [CI run 41507530278](https://github.com/PCakes303/agent-sandbox-security/actions/runs/41507530278) passed all 21 tests on Python 3.10, 3.11 and 3.12.
- Master staging packet refreshed and exact product parity verified: 15 remote files, 15 staged files, zero missing, extra or differing Git blob hashes.

**Disposition remains BLOCKED.** These changes harden only the policy parser/validator. No OS sandbox, resource enforcement, workload execution, authenticated identity, production policy, artifact-verification service, emergency-stop runtime or compliance integration exists. Privileged execution remains prohibited.

## Findings and remaining exceptions

1. **Blocking parser resource limits:** `load_policy(raw)` accepts unbounded input and calls `json.loads` before enforcing byte-size or nesting-depth limits. Deeply nested input may raise `RecursionError`, which is not normalized to `PolicyError`. Add a strict byte ceiling before parse, depth limit, and controlled parser-error handling.
2. **Unbounded collections:** filesystem path arrays and egress allowlists lack item-count limits; path and egress strings need explicit bounds. Add limits and negative tests.
3. **Schema/validator divergence:** CI does not execute Draft 2020-12 schema validation. The schema is less restrictive than the runtime validator: it permits `execution.allow_execution=true`, relative/traversal paths, and does not express numeric ceilings or all strict path/network semantics. Reconcile the normative schema and runtime contract, then test schema/runtime agreement.
4. **Private reporting route unverified:** SECURITY.md now states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private route.
5. **GitHub About metadata incomplete:** live description, homepage and topics are empty. Apply and verify actual About settings.
6. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
7. **License pending:** no root LICENSE file or GitHub license declaration was observed. Do not assume reuse/redistribution rights.
8. **Dependencies untested:** identity-trust, policy-engine, audit-provenance, secure-supply-chain, emergency-control and compliance-governance remain declared-only; no tested combinations exist.
9. **No isolation or execution:** policy validation is not enforcement. No backend applies filesystem, network, syscall, CPU, memory, time, process, IPC or tenant isolation. Keep privileged execution prohibited.

## Acceptance to clear BLOCKED

- Enforce byte-size and nesting-depth limits before/while parsing; normalize parser recursion failures into controlled policy errors.
- Bound filesystem/egress collections and strings.
- Make the Draft 2020-12 schema and reference validator agree, and validate both in CI with negative cases.
- Verify private vulnerability reporting, GitHub About metadata and repository administration settings.
- Keep licensing pending until explicitly approved.
- Do not enable execution until a separately reviewed OS isolation backend, independent emergency-stop authority, authenticated identity, fresh policy enforcement, artifact verification/revocation, audit and compliance integration, and adversarial conformance evidence exist.

A passing CI matrix validates 14 tests and the non-executing reference implementation. It does not prove OS isolation, workload containment, emergency-stop enforcement, compliance, or production security.
