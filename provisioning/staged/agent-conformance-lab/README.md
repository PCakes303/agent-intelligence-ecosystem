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

The repository documents the ecosystem's intended scoped mixed-license policy: Apache-2.0 for eligible original code and machine-readable contracts, and CC BY 4.0 for eligible original human-readable documentation. The manifest remains `pending-review` until contributor authority, file-level provenance and third-party notices are checked. Do not assume every file is cleared for redistribution. Datasets, evidence, fixtures, sample payloads, media and uncertain-provenance material receive no blanket license. See [LICENSE.md](LICENSE.md).
