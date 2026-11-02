# Staging Status — agent-conformance-lab

- Portfolio ID: conformance-lab
- Canonical registry position: 30 of 32 (29th component; master is position 1)
- GitHub owner: PCakes303
- Intended visibility: public
- Remote repository: not yet created; the connected GitHub integration cannot create repositories.
- Staging state: initial scaffold prepared in the master repository.
- Maturity: local metadata/fixture validator and deterministic report builder only.
- License: scoped mixed-license policy included in staged LICENSE.md; file-level provenance clearance remains required.
- Dependencies: foundation spec, schema registry, AIX core/codecs, transport gateway, swarm runtime, identity trust, policy engine, audit provenance, secure supply chain, emergency control and compliance governance (declared only).
- Implemented in this staging packet: local manifest/capability/compatibility consistency checks; synthetic AIX envelope schema; conformance report builder with PASS/FAIL/BLOCKED semantics; report digest; synthetic tests; Python 3.10–3.12 CI.
- Not implemented: arbitrary code execution, live interoperability, production swarm benchmarking, security certification or compliance certification.
- Required before remote deployment: owner creates public repository PCakes303/agent-conformance-lab, then the staging product files are pushed and CI verified.
- Required before production: satisfy every gate in docs/INTEGRATION-GATES.md and keep missing evidence BLOCKED.
