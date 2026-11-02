# Component Audit — agent-tool-adapters — 2026-11-02

**Repository:** [PCakes303/agent-tool-adapters](https://github.com/PCakes303/agent-tool-adapters)  
**Audited implementation commit:** `0419e80fabe1a3c1d5597043c86a49eba113e46d`  
**Baseline CI:** [Run 41432479875](https://github.com/PCakes303/agent-tool-adapters/actions/runs/41432479875) — success; 20 tests on Python 3.10, 3.11 and 3.12  
**Remediation commits:** `775e96309800937009560014aa50ae6e0ba1b154`, `686b2ea6af38f947fa0d30b252b67358baa146a0`  
**Latest remediation CI:** [Run 41499413474](https://github.com/PCakes303/agent-tool-adapters/actions/runs/41499413474) — in progress at checkpoint creation  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental synchronous in-process adapter registry with injected policy callback and bounded JSON payload checks; not a sandbox or production authorization boundary.

## Verified implementation

- Adapter registration is explicit and deterministic; duplicate adapter IDs and duplicate capability ownership are rejected.
- Invocation requires an exact registered capability and an injected policy callback. Missing, exceptional, non-PolicyDecision, or denying policy results fail closed.
- Input and output are checked against JSON-compatible types, string-only object keys, finite numbers, cycle rejection, configurable serialized UTF-8 byte ceiling (default 1 MiB), and configurable nesting depth (default 64).
- Adapter exceptions are converted to generic error codes; descriptors are deterministic and capability declarations are snapshotted at registration.
- Twenty unit tests cover policy allow/deny/error, capability and registration conflicts, payload byte/depth bounds, invalid JSON values, cycles, output limits, adapter exceptions and descriptor determinism.
- CI passed on Python 3.10, 3.11 and 3.12 in baseline run 41432479875.
- Capability metadata correctly limits tested capabilities to registration, policy-gated invocation seam and bounded JSON payloads. Compatibility metadata declares AIX Core, Transport Gateway, Policy Engine and Sandbox Security but has no tested combinations.
- The implementation is synchronous and in-process. It has no authentication, process isolation, execution timeout/cancellation, remote transport, durable audit, credential brokering or production policy-engine integration.
- License is pending review; no license was added.

## Corrections committed during audit

- `775e96309800937009560014aa50ae6e0ba1b154`: corrected README to state that `agent-sandbox-security` exists as an experimental contract scaffold but does not provide OS isolation or workload execution.
- `686b2ea6af38f947fa0d30b252b67358baa146a0`: clarified that no dedicated private reporting address is published and an approved private route must be configured if GitHub private reporting is unavailable.
- Created [issue #1](https://github.com/PCakes303/agent-tool-adapters/issues/1) for identifier/descriptor limits, malformed direct invocation handling, private reporting, metadata and staging evidence.

## Findings and remaining exceptions

1. **Unbounded registry metadata:** adapter IDs, capability identifiers, principal IDs and policy decision IDs have no explicit maximum length. Registration also permits arbitrarily large capability sets and descriptor catalogs. Add identifier and collection-count limits.
2. **Descriptor schema is not enforced:** CI tests the runtime registry but does not execute the descriptor JSON Schema. Schema fields such as adapter IDs/capabilities lack maximum lengths and capability arrays lack `maxItems`. Either complete and validate the schema or explicitly treat it as an informational contract.
3. **Direct API input precondition:** `invoke` assumes an `Invocation` instance with expected attributes; malformed direct-call objects can raise before returning a structured denial. Decide whether this is a trusted-host precondition or validate invocation shape at the public API boundary.
4. **Private reporting route unverified:** SECURITY.md now states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private channel.
5. **GitHub About metadata incomplete:** live description, homepage and topics are empty. Apply and verify actual About settings.
6. **Staging evidence missing in repo:** `STAGING-STATUS.md` is absent. Master staging records claim exact blob parity; refresh and preserve evidence if parity is to be asserted as current.
7. **License pending:** no root LICENSE file or GitHub license declaration was observed. Do not assume reuse/redistribution rights.
8. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
9. **No tested integrations:** AIX, transport, policy and sandbox dependencies are declarations only. The sandbox-security component itself does not yet provide OS isolation.

## Acceptance to clear BLOCKED

- Add bounded adapter/capability/principal/decision identifiers and capability/catalog count limits.
- Complete descriptor schema constraints and validate them in CI, or clearly document the schema's non-enforced status.
- Validate malformed direct invocation objects or state the trusted-host API precondition explicitly and test it.
- Verify a private vulnerability reporting route, About metadata and repository administration settings.
- Refresh staging-to-remote blob-SHA parity and retain evidence.
- Keep all production security and cross-repository interoperability claims gated on authenticated identity, real policy enforcement, transport integration, OS isolation, timeout/resource controls and reproducible integration tests.

A passing three-version CI matrix validates the current 20 tests only. It does not establish authentication, authorization enforcement, sandboxing, time-bounded execution, cross-repository interoperability or production readiness.
