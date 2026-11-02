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

## Post-audit direct-input and resource-boundary hardening — 2026-11-02

A deeper review confirmed the original findings and additional gaps: adapter/capability identifiers and sets were unbounded; malformed objects passed directly to invoke() could raise before returning a structured denial; policy decision IDs were unbounded; and payload traversal had no total-item budget. The descriptor schema also disagreed with the actual descriptors() output (it required a version field that the runtime does not emit) and was not validated in CI.

Corrections committed:
- 52453cbb59198b4586962492c3ab3a3d6e904237: added bounded identifier formats, 128-capability per-adapter cap, 10,000-adapter registry cap, payload item budget and hard payload-byte/depth ceilings; malformed direct invocation, invalid principals, missing callbacks and invalid decision IDs now fail closed.
- 542bb7e18dd15b00fe6b194e12dd41e9dd2f198d: corrected payload-item accounting so container exit markers are not counted as JSON values.
- a3580c7d0479ecde979ad58eeb6b6091ac456165 and 3e4f3cdc691abd8eab64f74870abe473df1b55bf: added tests for malformed direct invocation, missing policy, decision-ID bounds, adapter/capability bounds, payload-item bounds and configuration limits.
- f652db7117dc37bf6f1a0ffed0440875d581dcad: aligned descriptor schema with actual runtime descriptor fields and bounded identifier/capability arrays.
- e57ecd42ce2e8f88ece2a80afd5b17559e8369d2 and 90d380c46c033d7dd7452cec982d57f3dbe146a5: added pinned jsonschema development dependency and CI installation so descriptor schema is exercised by tests.
- a2250831c00fe1a59e0f8b314f0e1b9db6034a59, f5f084f6054bb8d18ce1c0cea90634ade9fd8400, 7c58e0e42983d76904ffa0d8fe64525a6aeef909 and 519cfa36249f28e66ba020d0e71e4f7dffbc2917: updated contract, security, capability metadata and README test count.
- Final CI after schema/requirements integration was still running at checkpoint update; verify the completed 27-test Python 3.10–3.12 matrix before claiming it passed.

The repository remains BLOCKED: no authentication, production policy service, sandbox, timeout/cancellation, durable audit or third-party adapters are implemented.

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
