# Security Policy

This repository is an experimental, bounded, in-memory discovery index. It is not a production discovery service, cryptographic verifier, identity provider, or authorization system.

## Reporting

Do not publish exploitable vulnerabilities, credentials, private keys, or sensitive operational data in public issues. Use GitHub private vulnerability reporting or a private security advisory if enabled for this repository. A dedicated private reporting address is not published here; if private reporting is unavailable, the owner must configure an owner-approved private channel before production use.

## Trust and resource boundaries

- Discovery records are untrusted claims. A record passing local validation does not prove its publisher, endpoint ownership, availability, safety or advertised capability.
- Signature-verifier and issuer-trust callbacks are integration seams. Only explicit boolean `True` is accepted; no cryptographic verifier or production identity integration is included.
- Record strings, capability collections, lifetime and registry count are bounded by the local contract. Network-facing adapters still require rate limits, quotas, body-size limits and abuse controls.
- The index is in-memory and process-local. It does not provide distributed consistency, federation, gossip, Sybil resistance or durable revocation state.
- Consumers must authenticate discovered endpoints independently and authorize every action separately.
