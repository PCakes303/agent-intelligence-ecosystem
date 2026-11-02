# Agent Federation Network

Portfolio ID: federation-network  
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

License selection remains pending portfolio review. No license is asserted.

## Licensing

This repository applies the ecosystem's scoped mixed-license policy: original source code and machine-readable contracts are licensed under Apache-2.0; original human-readable documentation is licensed under CC BY 4.0. Third-party material retains upstream terms. Datasets, evidence, fixtures, sample payloads, media, and material with uncertain provenance are not blanket-licensed and require separate review. See [LICENSE.md](LICENSE.md).
