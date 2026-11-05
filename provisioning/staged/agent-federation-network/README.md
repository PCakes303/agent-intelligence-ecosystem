# Agent Federation Network

Portfolio ID: federation-network  
Version: 1.0.0  
Maturity: research scaffold; local peer-policy contract validator only.

This repository defines safety contracts for federation between independently operated agent networks.

## Non-goals and safety boundary

The current scaffold validates a local peer declaration. It does not establish peer identity, verify signatures, exchange credentials, authorize remote work, propagate emergency stops, connect networks, or execute workloads. A valid record is not proof that a peer is trustworthy.

Federation must preserve independent administrative control. Trust is explicit, scoped, time-bounded, revocable, and fail-closed. A peer cannot grant itself trust by publishing metadata.

## Dependencies

Identity/trust, discovery, swarm coordination, policy, audit provenance, secure supply chain, emergency control and compliance governance are declared architecture dependencies. They are not yet verified runtime integrations.

## Development

Python 3.10+:

    python -m pip install -r requirements-dev.txt
    python -m unittest discover -s tests -v

See docs/FEDERATION-CONTRACT.md and docs/THREAT-MODEL.md.

## Licensing

This repository documents the intended scoped mixed-license policy. Its manifest remains `pending-review` until contributor authority, file-level provenance and third-party notices are checked. Do not assume every file is cleared for redistribution. Data, evidence, fixtures, sample payloads, media and third-party material receive no blanket license. See [LICENSE.md](LICENSE.md).
