# Component Audit — agent-resource-manifest — 2026-11-02

**Repository:** [PCakes303/agent-resource-manifest](https://github.com/PCakes303/agent-resource-manifest)  
**Audited commit:** `83edfac71c47d63f0c5d3a9735135308c8b72e15`  
**CI:** [Run 41489184208](https://github.com/PCakes303/agent-resource-manifest/actions/runs/41489184208) — all reported steps succeeded  
**Disposition:** **BLOCKED**  
**Maturity:** Scaffolded declarative resource contract and reference validator; not a package manager, publisher-authentication service or execution runtime.

## Verified implementation

- Draft 2020-12 JSON Schema exists at `schemas/resource-manifest.schema.json`.
- The schema defines required manifest fields, resource kinds, ID syntax, string limits, unique permission/dependency arrays, integrity structure and disallows additional properties.
- `examples/tool-resource.json`, documentation, validator, tests and starter build are present.
- `tools/validate_manifest.py` performs partial hand-written validation for core required fields, ID syntax, kind, duplicate permissions/dependencies and basic integrity metadata.
- Five unit tests cover valid input, invalid kind, duplicate permissions, invalid integrity algorithm and top-level type.
- `manifest.json`, `capabilities.json` and `compatibility.json` are present. The manifest and capability file correctly identify scaffolded maturity and pending license review. Compatibility dependencies are declared only; no tested combinations are recorded.
- README now explicitly states that no license has been approved and reuse/redistribution rights must not be assumed.
- `AGENTS.md` was corrected in commit `9bb1630b18dd74cafecf896b6f081e4544f37855` to use the PCakes303 / MrCakes931 scope and avoid unrelated accounts.
- CI run 41489184208 completed its requirements validator, unit tests and starter build steps successfully.

## Findings and exceptions

1. **Blocking security-reporting defect:** `SECURITY.md` still directs vulnerability reports to an unrelated GitHub profile. The manifest's `security_contact` is null, and no verified private reporting endpoint is recorded. Issue [#1](https://github.com/PCakes303/agent-resource-manifest/issues/1) tracks the required correction and reporting-channel setup.
2. **Blocking schema/validator drift:** the normative JSON Schema is not actually executed by CI. The hand-written validator does not enforce all schema constraints, including string max lengths and `additionalProperties: false`. CI currently validates the example only through this partial validator. Issue #1 tracks schema/validator conformance work.
3. **License pending:** no root `LICENSE` file or GitHub license declaration was observed. Do not add a license without an approved per-repository and per-artifact decision.
4. **GitHub About metadata incomplete:** live repository metadata has no description, homepage or topics.
5. **Compatibility not demonstrated:** all three declared dependencies are marked `declared`; `tested_combinations` is empty.
6. **Administration controls unverified:** branch protection and repository security-feature settings were not confirmed through the available integration.
7. **No runtime authority:** the project correctly disclaims resource execution, installation, publisher authentication and authorization grants based solely on manifest validity.

## Acceptance to clear BLOCKED

- Remove the unrelated account reference from `SECURITY.md` and configure/verify a private reporting route.
- Execute the normative JSON Schema in CI or bring the reference validator into demonstrable parity; add negative tests for all relevant schema constraints.
- Retain pending license and metadata status until approved decisions are applied.
- Add cross-repository consumer fixtures before claiming tested compatibility.

Passing CI confirms the current partial validator and tests run; it does not establish full JSON Schema conformance, publisher trust, authorization or safe execution.
