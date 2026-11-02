# Federation Contract (Draft)

## Independent domains

Each network retains its own operators, identities, policies, audit records, and emergency controls. Federation is not a common root of trust. No peer may mint or extend another peer's trust.

## Trust lifecycle

Peer trust is pending until independently authenticated, approved through an owner-controlled process, scoped, time-limited and auditable. Revocation and emergency STOP override all allow decisions. Trust does not transitively extend to downstream peers.

## Required runtime gates (not implemented)

1. Cryptographic peer authentication and key rotation.
2. Explicit bilateral trust and audience-bound scopes.
3. Local policy evaluation and authorization at both domains.
4. Revocation distribution with bounded staleness and fail-closed behavior.
5. Emergency STOP propagation, acknowledgement and recovery control.
6. Tamper-evident audit/provenance at both domains.
7. Supply-chain verification and pinned protocol/schema versions.
8. Independent compliance/applicability review.

## Current implementation

Only local declaration structure and policy-field validation exists. It returns REVIEW_REQUIRED for active declarations because identity/signature verification is absent. Pending, revoked, stopped and expired declarations are BLOCKED. It does not open sockets or exchange messages.
