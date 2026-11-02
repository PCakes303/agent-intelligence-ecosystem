# Component Audit — agent-transport-gateway — 2026-11-02

**Repository:** [PCakes303/agent-transport-gateway](https://github.com/PCakes303/agent-transport-gateway)  
**Audited baseline:** `1b2e5873f05364fc0c8f2c124bc76c640eeb3096`  
**Remediation commits:** `d6ba36e33e56a13a1744f26842c4164fbf42f229`, `88b0b3b5bab2661d52044a624f69dbf003599da2`, `eb0386832beb3e900a1bd9d2eafc9f9c0233a5dd`, `2452ecc50a9da260ee6f275bcba3f4faf71879db`, `a22240dbca0437d5e5a4dbebdf48c25e5eabcd28`, `ed1104d993d20759cd68642f93c2607ba870ded9`, `0d8bca7452fd5cc2e5f18fb8637edbb5defae487`, `d647bd08779a2526f641df25d97a3e046ca69618`  
**Final remediation CI:** [Run 41491823732](https://github.com/PCakes303/agent-transport-gateway/actions/runs/41491823732) — success on Python 3.10, 3.11 and 3.12; 18 tests per matrix job. Subsequent adversarial regression CI is tracked separately below.  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental, bounded single-process request guard; not a network gateway or production security boundary.

## Verified implementation

- Guard rejects missing/oversized principal, action, resource and nonce context; non-byte bodies; oversized bodies; invalid/non-finite timestamps; stale requests; missing authorizers; replays; denied authorization; and authorization exceptions.
- Replay cache is now bounded by configurable `max_replay_entries` (default 10,000). Capacity exhaustion fails closed rather than growing memory without limit.
- Configuration rejects non-positive/non-integer limits and non-finite timing values. Boolean timestamps are rejected. Clock exceptions and non-finite clock values fail closed.
- Authorization only allows explicit boolean `True`; truthy non-boolean responses are rejected.
- Replay state remains in-memory, volatile and process-local. It is not shared across workers, hosts, restarts or regions.
- CI matrix run 41491823732 passed on Python 3.10, 3.11 and 3.12; each job ran 18 unit tests.
- Capability metadata, contract, threat model, security policy and staging status were updated to describe the bounded cache and remaining limitations.
- License remains pending review; no license was added. Dependencies on AIX Core, AIX Codecs, Identity Trust and Policy Engine remain declared, not tested combinations.

## Corrections committed during audit

- `d6ba36e33e56a13a1744f26842c4164fbf42f229`: bounded replay-cache capacity, context lengths and config/timestamp validation; strict boolean authorization result; fail-closed clock handling.
- `88b0b3b5bab2661d52044a624f69dbf003599da2`: added eight negative/boundary tests for capacity, context limits, timestamp/clock handling, authorization result and configuration.
- `eb0386832beb3e900a1bd9d2eafc9f9c0233a5dd`: removed stale `13 / 29` portfolio count from README.
- `2452ecc50a9da260ee6f275bcba3f4faf71879db`: clarified private-reporting gap and trust boundary in SECURITY.md.
- `a22240dbca0437d5e5a4dbebdf48c25e5eabcd28`: updated threat-model rows for bounded replay and context controls.
- `ed1104d993d20759cd68642f93c2607ba870ded9`: aligned capability metadata with implemented behavior.
- `0d8bca7452fd5cc2e5f18fb8637edbb5defae487`: clarified strict authorization result and bounded replay contract.
- `d647bd08779a2526f641df25d97a3e046ca69618`: reconciled deployment and audit status.
- Created [issue #1](https://github.com/PCakes303/agent-transport-gateway/issues/1) for authentication, shared replay, protocol adapters, integration and governance gates.

## Post-audit adversarial back-check — 2026-11-02

A deeper boundary review found that math.isfinite() and float() can raise OverflowError for extremely large Python integers. The request guard accepted integer timestamps and timing configuration values, so these inputs could escape the intended stable-denial/validation behavior instead of failing closed.

- a0f92357c8b8503f52be75eb4e89bbecaa46d1c7: introduced safe finite-number conversion that rejects booleans, non-numeric values, overflow and non-finite values for timestamps, clocks and timing configuration.
- 51f721ff00d3dad27238760ca73fe84051183c74: added three regression tests for oversized integer timestamps, clocks and timing configuration.
- 282992ca615ae2633cf2c4a14069accdbefdf6bc: added explicit pending-license disclosure to README.
- CI for the new tests and README update was queued/in progress at this checkpoint update; final conclusion must be verified before claiming the latest head passed.

The request guard now rejects huge integer timestamp/clock/config values with stable outcomes rather than leaking numeric-conversion exceptions. This does not change the existing non-production limitations or clear the BLOCKED disposition.

## Findings and remaining exceptions

1. **No authenticated principal source:** the guard accepts a principal ID from its caller. No authenticator, credential validation or trusted identity integration is implemented.
2. **No production policy integration:** the authorizer is a callback seam. No authenticated, policy-versioned policy service, signed policy input or protected-resource enforcement is integrated.
3. **Replay is local only:** the bounded cache protects one process. It does not prevent replay across instances or restarts. A shared atomic nonce store, bounded retention and fail-closed store-outage behavior are required for multi-instance use.
4. **No AIX schema/codec integration:** the guard does not validate decoded messages against pinned AIX Core schemas or use AIX Codecs canonical decoding.
5. **No network listener or adapters:** no HTTP, MCP or A2A adapter exists. Protocol-native cancellation, timeout, retry and error behavior remain untested.
6. **Denial-of-service controls incomplete:** no rate limiting, quotas, connection budgets, streaming ingress limits, load tests or operational telemetry are implemented.
7. **Private reporting route unverified:** SECURITY.md now states that no dedicated private address is published. Verify GitHub private vulnerability reporting/security advisories or configure an owner-approved private channel.
8. **GitHub About metadata incomplete:** description exists; homepage and topics are empty. Apply and verify actual About settings.
9. **License pending:** no root LICENSE file or GitHub license declaration was observed; reuse and redistribution rights must not be assumed.
10. **Staging parity outstanding:** refresh staging-to-remote path/blob-SHA parity against current `main` before portfolio sign-off.
11. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.

## Acceptance to clear BLOCKED

- Implement trusted authentication and bind principal context to verified credentials.
- Integrate policy-engine decisions with authenticated policy version/provenance and protected-resource enforcement.
- Replace local replay state with bounded, shared, atomic replay reservation and test concurrent/multi-instance behavior.
- Add pinned schema/codec integration and protocol-specific HTTP/MCP/A2A adapters with end-to-end negative tests.
- Add rate limits, quotas, connection/resource budgets, audit integration, observability and load/adversarial tests.
- Verify private reporting, GitHub About metadata, repository settings and staging parity; record explicit license decision.

Passing CI validates this bounded prototype and its 18 tests on three Python versions. It does not establish caller identity, production authorization, distributed replay defense, network security, protocol conformance or production readiness.
