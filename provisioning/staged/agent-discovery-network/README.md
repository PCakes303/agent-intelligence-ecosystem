# Agent Discovery Network

**Portfolio position:** Repository 14 / 29 public  
**Layer:** Swarm  
**Maturity:** prepared scaffold; standalone remote not yet created  
**Dependencies:** Agent Resource Manifest, Agent Capability Registry, Agent Identity & Trust, Agent Transport Gateway

## Mission

Provide a bounded discovery index for agents, resources, services and capability advertisements. Nodes may publish endpoint records and query records that are current, structurally valid, signature-verified by an injected verifier, and accepted by an injected trust policy.

Discovery is not authentication, authorization, health verification, or proof that a discovered service is safe. A returned record is a candidate endpoint only. Callers must authenticate the remote peer and authorize every action through the appropriate identity and policy components.

## Initial implementation

The scaffold provides:
- a versioned discovery-record contract;
- strict required-field, URI, timestamp and expiry validation;
- an in-memory registry with deterministic expiry pruning;
- fail-closed signature-verification and trust-evaluation callbacks;
- query filtering by record kind, capability and issuer;
- unit tests for stale, invalid, untrusted and duplicate records.

The verifier and trust evaluator are explicit integration seams. No cryptographic key management, signature algorithm, identity issuance, network transport, gossip, federation or distributed storage is implemented.

## Security invariants

- Records must identify their issuer and source provenance.
- Records must have a bounded lifetime and must never be returned after expiry.
- Signature verification and trust evaluation are separate checks.
- Missing, failing or rejecting verifier/trust callbacks fail closed.
- A record's claims do not grant capabilities or permissions.
- Discovery does not bypass remote authentication or per-action authorization.
- The in-memory index is single-process prototype state, not a distributed source of truth.

## Run tests

Python 3.10+; standard library only.

```bash
python -m unittest discover -s tests -v
```

## Next gates

1. Deploy this scaffold and verify the Python CI matrix.
2. Bind records to the canonical Resource Manifest and Capability Registry schemas.
3. Integrate authenticated issuer identities and key rotation/revocation from Identity & Trust.
4. Specify and implement a cryptographic signature profile with test vectors.
5. Add authenticated publish/query APIs over the Transport Gateway.
6. Add bounded distributed storage, replication and stale-node reconciliation.
7. Add adversarial tests for equivocation, replay, poisoning, Sybil behavior and trust-policy changes.

No production discovery network, cryptographic signature verification, distributed consistency or federation is claimed.
