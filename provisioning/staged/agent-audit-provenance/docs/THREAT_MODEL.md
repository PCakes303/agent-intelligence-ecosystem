# Threat Model

## Assets
Audit records, event ordering, event integrity, operational metadata, and downstream trust decisions based on logs.

## Trust boundaries
Events are supplied by external producers. The local file and host filesystem are outside the verifier's trust guarantee. The CLI has no identity provider, remote collector, key store, or trusted clock.

## Threats addressed by the prototype
- Accidental edits to event fields: digest mismatch.
- Record modification: digest mismatch.
- Reordering or insertion within a chain: link/digest verification failure.
- Broken previous-hash continuity: verification failure.
- Malformed event structure: validation failure.

## Threats not addressed
- Malicious producer lying about an event.
- Forged actor identifiers.
- Log truncation or replacement when no external checkpoint is retained.
- Host compromise, filesystem rollback, or deletion.
- Digest replacement by an attacker who can rewrite the entire log.
- Non-repudiation, trusted timestamps, confidentiality, or authorization.
- Digital signatures and key compromise.

## Required production controls
Authenticated ingestion, signatures with managed keys, independently stored checkpoints, append-only or WORM storage, access control, retention and deletion governance, privacy review, monitoring, and independent security testing.
