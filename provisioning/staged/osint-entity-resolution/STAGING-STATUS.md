# Staging Status — osint-entity-resolution

- Portfolio ID: entity-resolution
- Canonical registry position: 23 of 32 (22nd component; master is position 1)
- GitHub owner: PCakes303
- Intended visibility: public
- Remote repository: deployed at https://github.com/PCakes303/osint-entity-resolution on main.
- Staging state: deployed; 23 product files match the remote exactly by path and Git blob SHA.
- Maturity: public non-personal candidate matcher; no identity resolution or graph writes.
- License: scoped mixed-license policy included in staged LICENSE.md; file-level provenance clearance remains required.
- Dependencies: osint-evidence, schema-registry, identity-trust, policy-engine, audit-provenance, emergency-control, compliance-governance, secure-supply-chain (declared only).
- Implemented in this staging packet: Draft 2020-12 entity/candidate schemas; deterministic normalization; bounded exact-identifier/alias/name candidate matching; human-review-required outputs; synthetic tests; Python 3.10–3.12 CI.
- Not implemented: people matching, personal profiling, automatic merge, identity assertion, network lookup, graph persistence, reviewer workflow or legal/compliance determination.
- Staging CI: master workflow run 41515580489 passed 16 tests on Python 3.10, 3.11 and 3.12. Remote CI workflow expression was corrected after its first run; successful remote matrix rerun remains pending.
- Deployment verification: 23/23 product paths match by Git blob SHA; zero missing, differing or extra product files. Remote CI must pass all Python matrix jobs before the deployment checkpoint is closed.
- Required before production: satisfy every gate in docs/INTEGRATION-GATES.md; production identity resolution remains explicitly out of scope for this profile.
