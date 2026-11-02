# Audit and Provenance — initial contract

**Status:** starter hash-chain utility and event schema in the master repository; dedicated repository not yet present.

## Starter
Use the existing event schema and [hash-chain helper](../../tools/audit_chain.py). The hash chain detects modifications relative to the records/checkpoint being verified; it does not prove truth, completeness, origin, or non-repudiation.

## Developer
Add canonical event types for identity, policy decisions, tool invocation, delegation, data access, build/release, and administrative changes. Include actor, action, target, outcome, event time, correlation ID, policy version, and evidence references where applicable.

## Production
Use authenticated event ingestion, append-only storage, access separation, retention controls, trusted timestamps where required, signed checkpoints, key rotation, alerting, export controls, and tamper-response procedures. Do not log secrets, raw credentials, or private model reasoning.
