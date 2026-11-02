# Discovery Contract v1

## Purpose

The discovery network locates candidate agents, resources and services. It does not authenticate callers, authorize actions, certify capability claims or guarantee endpoint availability.

## Record fields

| Field | Meaning |
|---|---|
| record_id | Unique identifier within the publishing registry |
| kind | One of agent, resource or service |
| subject_id | Stable identifier for the advertised subject |
| endpoint | HTTPS endpoint URI; embedded credentials are forbidden |
| issuer_id | Identity of the record publisher |
| issued_at / expires_at | Unix timestamps defining a bounded validity interval |
| capabilities | Capability identifiers claimed by the subject |
| provenance | Publishing source or node reference |
| signature | Opaque signature material evaluated by the configured verifier |

The initial dataclass is a local experimental contract. It is not yet bound to the canonical Resource Manifest or Capability Registry schemas.

## Publish requirements

A publisher must validate record structure and lifetime, verify the signature using an approved cryptographic profile, and evaluate issuer trust. The scaffold represents signature and trust checks as injected callbacks; only explicit boolean `True` accepts a record. It does not implement cryptography or identity lifecycle.

## Query requirements

Queries may filter by kind, capability and issuer. Expired records are removed and never returned. Signature and issuer trust are re-evaluated at read time so that a changed trust decision can hide a previously accepted record.

## Trust and authorization separation

A trusted issuer may still publish false or stale claims. A valid signature proves control of a signing key under the chosen profile, not the truth of a capability claim. Consumers must authenticate the discovered endpoint independently and authorize each action through the policy boundary.

## Expiry

The initial maximum record lifetime is configurable and defaults to 24 hours. Record identifier, subject, issuer, endpoint, provenance and signature strings have fixed upper bounds; capability collections and individual capability identifiers are bounded. Registry capacity is bounded and capacity exhaustion rejects publication. Records are rejected when expired, issued in the future, or longer-lived than the configured maximum. Production deployments must define clock-skew tolerance, renewal behavior, revocation and retention semantics.

## Storage and federation

The in-memory registry is process-local, bounded and non-durable. Replication, gossip, conflict resolution, tombstones, federation and distributed consistency are out of scope for this scaffold.
