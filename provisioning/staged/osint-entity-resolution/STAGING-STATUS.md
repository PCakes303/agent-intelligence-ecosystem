# Staging Status — osint-entity-resolution

- Portfolio ID: entity-resolution
- Canonical registry position: 23 of 32 (22nd component; master is position 1)
- GitHub owner: PCakes303
- Intended visibility: public
- Remote repository: not yet created; the connected GitHub integration cannot create repositories.
- Staging state: initial scaffold prepared in the master repository; matrix validated.
- Maturity: public non-personal candidate matcher; no identity resolution or graph writes.
- License: scoped mixed-license policy included in staged LICENSE.md; file-level provenance clearance remains required.
- Dependencies: osint-evidence, schema-registry, identity-trust, policy-engine, audit-provenance, emergency-control, compliance-governance, secure-supply-chain (declared only).
- Implemented in this staging packet: Draft 2020-12 entity/candidate schemas; deterministic normalization; bounded exact-identifier/alias/name candidate matching; human-review-required outputs; synthetic tests; Python 3.10–3.12 CI.
- Not implemented: people matching, personal profiling, automatic merge, identity assertion, network lookup, graph persistence, reviewer workflow or legal/compliance determination.
- Staging CI: master workflow run 41515580489 passed 16 tests on Python 3.10, 3.11 and 3.12.
- Required before remote deployment: owner creates public repository PCakes303/osint-entity-resolution, then the staging product files are pushed and repository CI verified.
- Required before production: satisfy every gate in docs/INTEGRATION-GATES.md.
