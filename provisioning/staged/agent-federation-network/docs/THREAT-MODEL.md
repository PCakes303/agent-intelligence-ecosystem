# Threat Model

## Assets

Domain autonomy, identity credentials, authorization scopes, revocation state, emergency STOP state, audit integrity, and availability.

## Adversaries and failure modes

Malicious or compromised peer; stolen signing key; stale discovery record; replayed trust declaration; privilege escalation through broad scopes; transitive trust confusion; revoked peer remaining connected; delayed STOP propagation; compromised supply chain; malformed or oversized metadata; clock skew; operator misconfiguration.

## Controls required before production

- Mutual cryptographic authentication with key rotation and revocation.
- Short-lived, audience-bound, least-privilege scopes.
- Explicit bilateral approval; no self-asserted trust.
- Replay protection, nonce/sequence handling and bounded clock skew.
- Local policy decisions at both domains; remote allow cannot override local deny.
- Fail-closed STOP and revocation handling with tested propagation SLOs.
- Signed audit events, immutable retention and provenance verification.
- Pinned dependencies, signed releases, SBOM and vulnerability response.
- Rate, size, depth and concurrency limits on all ingress.
- Isolation of protocol parsers from workload execution.

## Current state

This repository implements none of the production controls above. It validates a local JSON-like record only. A schema-valid record is not an authenticated peer.
