# Contributing

Run `python -m unittest discover -s tests -v` and review the federation contract and threat model.

Changes to trust states, scope, expiry, revocation, STOP semantics, or remote authorization require an ADR and negative tests. Do not add network clients, credential exchange, remote execution, or trust transitivity without a separately reviewed design and security gate.
