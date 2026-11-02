# Audit event and log contract

## Event fields

- `event_id`: producer-assigned unique identifier within its producer namespace.
- `timestamp`: RFC 3339 timestamp supplied by the producer; this component does not attest to clock accuracy.
- `event_type`: namespaced event classification.
- `actor`: claimed actor identifier and type; not authenticated by this prototype.
- `action`, `resource`: concise operation and target references.
- `outcome`: success, failure, denied, or unknown.
- `details`: structured, data-minimized event-specific fields.
- `previous_hash`: prior record digest, or null for the first record.
- `event_hash`: SHA-256 over canonical JSON of all event fields except event_hash.

## Canonicalization

Canonical bytes are UTF-8 JSON using sorted object keys, compact separators `(',', ':')`, and `ensure_ascii=false`. The event hash is lowercase hexadecimal SHA-256. Arrays retain order. Producers must not rely on semantically equivalent but byte-different values hashing identically.

## Chain semantics

The first record has `previous_hash: null`. Every following record points to the preceding record's `event_hash`. Verification checks required fields, each digest, and continuity.

A valid chain proves only internal consistency relative to the presented records. It does not prove completeness, authenticity, truth, or trusted time. A truncated suffix can be undetectable unless a prior digest is anchored outside the log.
