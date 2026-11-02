# Component Audit — agent-schema-registry — 2026-11-02

**Repository:** [PCakes303/agent-schema-registry](https://github.com/PCakes303/agent-schema-registry)  
**Audited commit:** `07ac22d952682c40dbe4b70d4209744e81f274d0`  
**CI:** [Run 41407422248](https://github.com/PCakes303/agent-schema-registry/actions/runs/41407422248) — success  
**Disposition:** **BLOCKED**  
**Maturity:** Scaffolded schema catalog and structural checker; semantic compatibility analysis is explicitly planned, not implemented.

## Verified implementation

- The repository contains a Draft 2020-12 common metadata schema, a structural catalog checker, unit tests, docs and starter CI.
- The checker verifies that schema files parse, have `$schema`, `$id`, `title` and `type`, use the declared Draft 2020-12 dialect, and have unique IDs.
- Three tests cover schema parsing, dialect declaration and unique IDs.
- README correctly states that the standard-library checker is not a full JSON Schema semantic validator and directs consumers to use a conformant validator.
- `manifest.json`, `capabilities.json` and `compatibility.json` are present. Semantic compatibility analysis is correctly marked planned; no tested dependency combinations are claimed.
- CI run 41407422248 passed the catalog checker, unit tests and starter build.

## Findings and exceptions

1. **Blocking security-reporting/account-scope defect:** `AGENTS.md` and `SECURITY.md` still refer to an unrelated GitHub profile. The manifest has `security_contact: null`; no verified private vulnerability-reporting route is recorded.
2. **License disclosure incomplete:** manifest status is `pending-review`, and no root `LICENSE` file or GitHub license declaration was observed, but README does not clearly state the license status or that reuse rights must not be assumed.
3. **GitHub About metadata incomplete:** live metadata has no description, homepage or topics.
4. **Limited catalog coverage:** the current checker and tests are structural; they do not semantically validate schemas or analyze backward/forward compatibility. README and capabilities metadata correctly disclose this.
5. **Schema examples/conformance remain partial:** the published schema set is minimal. Add positive/negative fixtures and conformant semantic validation before promoting schemas to stable.
6. **Compatibility not demonstrated:** the foundation dependency is declared only; no tested combinations are recorded.
7. **Administration controls unverified:** branch protection and repository security-feature settings were not confirmed through the available integration.

## Acceptance to clear BLOCKED

- Remove unrelated account references and configure/verify a private vulnerability-reporting route.
- Add explicit README license-status disclosure while retaining pending status until approved.
- Apply and verify About metadata after the description and topics are grounded in actual implementation.
- Add positive/negative schema fixtures and conformant validation where required; keep compatibility analysis marked planned until tested.
- Publish consumer/provider compatibility evidence before marking dependencies tested.

Passing CI confirms the current structural catalog checker and tests run. It does not prove full JSON Schema semantic validity, compatibility, authorization or production readiness.
