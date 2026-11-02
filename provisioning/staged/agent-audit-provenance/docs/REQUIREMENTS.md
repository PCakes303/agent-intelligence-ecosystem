# Requirements

## Functional
- Accept a structured audit event with required actor, action, resource, outcome, timestamp, and details.
- Reject malformed records and caller-supplied digest fields during append.
- Produce deterministic SHA-256 event digests.
- Link each event to the previous event digest.
- Verify every digest and link in an existing JSONL file.
- Return a non-zero exit status for invalid input or corrupted logs.

## Security and privacy
- Treat log content as untrusted.
- Do not claim producer identity authentication or event truth.
- Avoid collecting secrets and unnecessary personal information.
- Make integrity limitations explicit, especially truncation and missing external checkpoints.
- Keep the initial implementation dependency-free and inspectable.
