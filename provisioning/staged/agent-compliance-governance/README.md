# Agent Compliance Governance

Portfolio ID: compliance-governance  
Maturity: scaffolded governance register, control catalogue and evidence-index validator.

A machine-readable legal-monitoring register and AI/privacy governance control catalogue for the MrCakes931 Agent Intelligence Ecosystem.

## Important boundary

This repository is not a law firm, legal adviser, compliance officer, regulator, audit firm or certification body. It does not determine whether a law applies to a particular entity, provide legal advice, certify compliance, or prove that a control is operating. Its legal records are source-linked monitoring entries and require qualified counsel to determine applicability.

The initial register includes Colorado sources because the ecosystem owner is based in Denver, Colorado. Location alone does not establish that any law applies. Applicability depends on the entity, data, users, products, processing purposes, thresholds, sectors and actual deployment footprint.

## Current scaffold

- Strict validation of legal instrument and regulatory-monitor records.
- Control catalogue with explicit proposed/not-implemented status.
- Populated evidence tracker with one explicit evidence-gap entry per proposed control; collected evidence remains separately counted and requires a real artifact, digest, source, and review.
- Colorado monitoring records for the Colorado Privacy Act, SB26-189, HB26-1263, related rulemaking and a federal court litigation monitor.
- NIST AI RMF recorded as voluntary guidance, not binding law.
- Tests for schema validity, duplicate IDs, invalid statuses, source references, strict JSON parsing and resource limits.

## Quick start

Python 3.10+:

    python -m pip install -r requirements-dev.txt
    python -m compliance_governance.validate_registry
    python -m unittest discover -s tests -v

## No compliance claim

The initial control catalogue is proposed. No organizational controls have been implemented or evidenced by this repository. The evidence tracker contains 11 explicit not-collected gap records (one per proposed control) and zero collected evidence artifacts. Gap records describe what must be supplied; they are not evidence and must never be treated as proof of implementation, effectiveness, or compliance.

## Licensing

This repository applies the ecosystem's scoped mixed-license policy: original source code and machine-readable contracts are licensed under Apache-2.0; original human-readable documentation is licensed under CC BY 4.0. Third-party material retains upstream terms. Datasets, evidence, fixtures, sample payloads, media, and material with uncertain provenance are not blanket-licensed and require separate review. See [LICENSE.md](LICENSE.md).

The license declaration does not replace item-level provenance and third-party rights review before release.
