# Agent Emergency Control

Portfolio ID: emergency-control  
Maturity: scaffolded reference contract and validator.

Independent emergency-stop command and state-transition contracts for the MrCakes931 Agent Intelligence Ecosystem.

## Safety boundary

This scaffold validates command envelopes and evaluates deterministic stop/resume transitions. It does not authenticate signatures, issue credentials, persist authoritative state, revoke identities, contact agents, propagate commands, quarantine processes, or enforce a stop at an operating-system/runtime boundary. Those functions require separately reviewed adapters and integration tests. A passing validator is not an operational kill switch.

No privileged workload may execute on the strength of this repository alone. Until independent authority, durable state, revocation, propagation, enforcement and recovery paths are implemented and tested, consumers must fail closed.

## Contract decisions

- Stop commands require verified authority, freshness and revocation evidence.
- STOP is monotonic and takes precedence over ordinary policy decisions.
- Epochs increase strictly; replayed or stale commands are rejected.
- A stop remains active until an explicit, separately authorized resume; command expiry never auto-clears a stop.
- RESUME requires two distinct approvers, verified by a trusted identity adapter, plus a positive resume-policy decision.
- State is scoped; a transition for one scope cannot overwrite an active stop for another scope.
- The core is pure and dependency-injected. It contains no network client, persistence backend, credential store or process-control implementation.

## Quick start

Python 3.10+:

    python -m pip install -r requirements-dev.txt
    python -m unittest discover -s tests -v

See docs/COMMAND-CONTRACT.md, docs/THREAT-MODEL.md and docs/INTEGRATION-GATES.md.

## Dependencies

The master registry declares foundation, identity-trust, policy-engine, audit-provenance and secure-supply-chain as contract prerequisites. They are declared only; runtime interoperability is not claimed.

## Licensing

This repository applies the ecosystem's scoped mixed-license policy: original source code and machine-readable contracts are licensed under Apache-2.0; original human-readable documentation is licensed under CC BY 4.0. Third-party material retains upstream terms. Datasets, evidence, fixtures, sample payloads, media, and material with uncertain provenance are not blanket-licensed and require separate review. See [LICENSE.md](LICENSE.md).

License and third-party provenance still require human review before release.
