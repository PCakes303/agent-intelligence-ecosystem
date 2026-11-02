# Threat Model

## Assets
- Discovery record integrity and issuer provenance
- Endpoint and capability metadata
- Trust-policy decisions and revocation state
- Registry availability and bounded resource use
- Freshness and expiry state

## Threats and initial controls

| Threat | Initial control | Remaining limitation |
|---|---|---|
| Malformed record injection | Strict local field, URI and timestamp validation | Canonical cross-repository schema binding is pending |
| Expired/stale record | Required expiry, maximum lifetime, query-time expiry check | No distributed clock or renewal protocol |
| Forged record | Required opaque signature plus injected verifier | No cryptographic verifier or key lifecycle is implemented |
| Untrusted issuer | Injected trust evaluator at publish and query time | No production Identity & Trust adapter |
| Trust revocation | Re-evaluate issuer trust on every query | Revocation freshness depends on callback implementation |
| Registry exhaustion | Configurable record-count bound | No network rate limits or quotas |
| Duplicate identifier | Reject duplicate record IDs | No distributed conflict resolution |
| Capability laundering | Treat capabilities as unverified claims, not permissions | No capability certification or conformance proof |
| Endpoint compromise | Require consumers to authenticate endpoints independently | No endpoint health or ownership verification |
| Sybil/equivocation attacks | No claim of mitigation | Requires authenticated enrollment, reputation/limits and distributed analysis |

## Security boundaries

Discovery returns candidate metadata only. It must not create identities, grant permissions, establish sessions or authorize invocation. Network publication and lookup must be authenticated by a future transport integration.

## Non-goals

No production cryptography, distributed storage, gossip, federation, Sybil resistance, endpoint health checking or capability certification is included.
