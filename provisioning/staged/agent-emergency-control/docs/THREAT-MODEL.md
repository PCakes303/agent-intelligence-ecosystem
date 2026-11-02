# Threat Model

## Assets

- Availability of an independent emergency-stop path.
- Integrity and freshness of stop/resume commands and monotonic epochs.
- Integrity of per-scope state and approval evidence.
- Confidentiality of credentials and incident details.
- Correct propagation and acknowledgement of stop state by future enforcement points.

## Trust boundaries

- Command JSON and all fields are untrusted.
- Actor IDs, approver IDs, key IDs, signatures and role claims are untrusted until cryptographically verified against an authoritative identity and revocation service.
- Policy decisions are untrusted until authenticated and freshness-checked.
- Persistence, audit and propagation adapters are separate trust boundaries.
- The reference reducer is not an enforcement point.

## Threats and controls

| Threat | Reference control | Remaining requirement |
|---|---|---|
| Duplicate-key or parser ambiguity | Duplicate JSON keys and non-standard numeric constants rejected | Fuzz parser and test alternate encodings |
| Resource exhaustion | 64 KiB command limit and 16-level JSON depth limit | Rate limits and bounded queues in service |
| Replay / rollback | Strictly increasing per-scope epoch | Durable atomic compare-and-swap and consensus semantics |
| Forged or unauthorized stop | Explicit verifier protocol; missing evidence denies | Real signature, identity, role and revocation integration |
| Unauthorized resume | Two distinct approvers and requester separation; verifier evidence and policy gate | Cryptographic quorum verification and audited approval UX |
| Stop cleared by expiry | Active stop has no automatic expiry transition | Durable state and consumer leases must fail closed |
| Scope confusion | Exact scope matching; active scope cannot be overwritten | Hierarchical scope aggregation and distributed policy |
| Network partition | No networking implemented | Consumer-side stop leases, retries, acknowledgements and partition tests |
| Audit outage | No audit integration implemented | Durable append and independent audit retention |
| Partial propagation | No propagation integration implemented | Two-phase resume, acknowledgements and fail-closed consumers |
| Control-plane compromise | No key custody implemented | Offline root, key rotation, threshold authority and recovery procedures |

## Non-goals

This scaffold does not terminate processes, revoke credentials, quarantine nodes, isolate workloads, guarantee availability or provide a production kill switch. Do not deploy it as a sole control.
