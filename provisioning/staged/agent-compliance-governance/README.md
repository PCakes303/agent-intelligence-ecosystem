# Agent Compliance Governance

Portfolio ID: compliance-governance  
Maturity: scaffolded governance register, control catalogue and evidence-index validator.

A machine-readable legal applicability register and AI/privacy governance control catalogue for the MrCakes931 Agent Intelligence Ecosystem.

## Important boundary

This repository is not a law firm, legal adviser, compliance officer, regulator, audit firm or certification body. It does not determine whether a law applies to a particular entity, provide legal advice, certify compliance, or prove that a control is operating. Its legal records are source-linked monitoring entries and require qualified counsel to determine applicability.

The initial register includes Colorado sources because the ecosystem owner is based in Denver, Colorado. Location alone does not establish that any law applies. Applicability depends on the entity, data, users, products, processing purposes, thresholds, sectors and actual deployment footprint.

## Current scaffold

- Strict validation of legal instrument and regulatory-monitor records.
- Control catalogue with explicit proposed/not-implemented status.
- Evidence index schema with integrity and provenance fields.
- Colorado monitoring records for the Colorado Privacy Act, SB26-189, HB26-1263, related rulemaking and a federal court litigation monitor.
- NIST AI RMF recorded as voluntary guidance, not binding law.
- Tests for schema validity, duplicate IDs, invalid statuses, source references, strict JSON parsing and resource limits.

## Quick start

Python 3.10+:

    python -m pip install -r requirements-dev.txt
    python -m compliance_governance.validate_registry
    python -m unittest discover -s tests -v

## No compliance claim

The initial control catalogue is proposed. No organizational controls have been implemented or evidenced by this repository. The empty evidence index is intentional. Do not mark a control compliant because it exists in the catalogue.

## Licensing

License selection is pending portfolio review. No license is asserted.
