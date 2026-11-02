# AIX Task Lifecycle

This is the initial lifecycle contract. It describes protocol state, not a guarantee that a remote action occurred exactly once.

## States

- `proposed`: sender has issued a request; no acceptance is implied.
- `accepted`: receiver has accepted responsibility for attempting the task.
- `rejected`: receiver declined the task; include a machine-readable reason in a future stable error contract.
- `queued`: accepted work is waiting for execution.
- `running`: execution has started.
- `blocked`: progress requires an external condition or input.
- `succeeded`: receiver reports successful completion and references result evidence.
- `failed`: receiver reports unsuccessful completion.
- `cancelled`: work was cancelled; cancellation may race with completion.
- `expired`: deadline or lease expired according to the receiver's declared clock/lease policy.

## Required behavior

1. Every request has a unique message ID and stable task ID.
2. Retried submissions use an idempotency key scoped to the sender and task operation.
3. Duplicate submissions with the same idempotency key must not silently create duplicate side effects.
4. Acknowledgement is not acceptance; acceptance is not completion.
5. State updates carry correlation/trace and causation references.
6. Deadline handling is explicit; late results are not silently treated as on-time success.
7. Cancellation is best-effort unless the execution system can prove stronger semantics.
8. Receivers validate authorization and referenced-resource access independently of the envelope.

## Candidate transition graph

```text
proposed -> accepted -> queued -> running -> succeeded
    |           |         |         |-> failed
    |           |         |         |-> blocked -> running
    |           |         |         |-> cancelled
    |           |         |         |-> expired
    |           |         |-> cancelled / expired
    |           |-> rejected
    |-> rejected
```

Invalid transitions must be rejected or represented as explicit protocol errors. The exact retry, lease, and cancellation semantics require further conformance tests before AIX can be considered stable.
