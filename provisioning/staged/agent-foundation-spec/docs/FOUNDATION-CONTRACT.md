# Foundation contract

## Status
Scaffolded normative baseline. This document establishes initial requirements; it is not a certification of downstream implementations.

## Principles
- Explicit trust boundaries and least privilege.
- Deny-by-default authorization and fail-closed behavior.
- Versioned interfaces, documented compatibility, and migration paths.
- Provenance-aware evidence; a content hash establishes byte identity relative to a trusted reference, not truth or completeness.
- Resilient distributed behavior: idempotency, bounded retries, backpressure, and explicit partial failure.
- Human review for consequential decisions.

## Traceability
Requirements are machine-readable in [requirements/requirements.json](../requirements/requirements.json). Changes to normative requirements require an ADR or equivalent rationale, impact assessment, and tests in affected repositories.
