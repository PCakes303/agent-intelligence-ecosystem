# Agent Conformance Lab

Portfolio ID: conformance-lab  
Maturity: scaffolded contract/fixture validator and deterministic report builder.

Validate repository metadata, protocol fixtures and explicitly declared security/conformance gates across the MrCakes931 Agent Intelligence Ecosystem.

## Safety boundary

This scaffold validates local manifests, capability/compatibility declarations, JSON fixtures and supplied test results. It does not execute untrusted repositories, launch agents, connect to swarms, perform live network interoperability, benchmark production systems or certify security/compliance.

A local fixture pass is not cross-repository interoperability evidence. A conformance report must distinguish PASS, FAIL and BLOCKED and include limitations and evidence references. Dependencies remain declared until reproducible integration tests run against pinned remote artifacts. Accordingly, dependency evidence arrays and `tested_combinations` are intentionally empty; they must be populated only after real, reproducible integration tests produce reviewable evidence. These empty arrays are explicit non-claims, not unfinished fixture placeholders.

## Quick start

Python 3.10+:

    python -m pip install -r requirements-dev.txt
    python -m unittest discover -s tests -v

See docs/CONFORMANCE-CONTRACT.md, docs/SECURITY-GATES.md and docs/INTEGRATION-GATES.md.

## Licensing

This repository applies the ecosystem's scoped mixed-license policy: original source code and machine-readable contracts are licensed under Apache-2.0; original human-readable documentation is licensed under CC BY 4.0. Third-party material retains upstream terms. Datasets, evidence, fixtures, sample payloads, media, and material with uncertain provenance are not blanket-licensed and require separate review. See [LICENSE.md](LICENSE.md).
