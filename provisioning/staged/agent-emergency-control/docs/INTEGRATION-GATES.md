# Integration and Production Gates

A repository release or passing unit suite does not satisfy these gates. No privileged workload may execute until the relevant controls are implemented and independently verified.

1. **Authority:** integrate with agent-identity-trust for cryptographic signature verification, principal roles, key rotation and revocation. No local trust-on-first-use or self-asserted roles.
2. **Policy:** integrate agent-policy-engine for resume authorization and applicable control checks. STOP remains available when policy is unavailable.
3. **Durable state:** implement atomic monotonic per-scope state with rollback resistance, recovery, replication and tamper evidence.
4. **Audit:** integrate agent-audit-provenance. STOP must still activate during audit failure; the event must be durably queued and surfaced as a critical integrity fault.
5. **Propagation:** implement authenticated, bounded stop delivery, idempotency, retries, acknowledgements, partition handling and consumer leases.
6. **Resume protocol:** implement prepare/commit so consumers do not resume before the authoritative transition and quorum evidence are committed.
7. **Enforcement:** connect every runtime, worker, adapter and sandbox admission point. Verify actual process/workload denial and quarantine; message delivery is not enforcement.
8. **Supply chain:** verify signed builds, provenance and artifact identity through agent-secure-supply-chain.
9. **Conformance:** add adversarial tests for forged commands, replay, rollback, clock skew, partitions, partial acknowledgements, restart, storage corruption and compromised approvers.
10. **Operations:** define on-call ownership, offline break-glass procedures, key recovery, incident response and safe reactivation. No unsupported response SLA.

Until every applicable gate is evidenced, this repository remains a scaffold and all dependent execution paths must remain disabled.
