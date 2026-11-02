# Agent Skill Library — staging status

**Portfolio repository:** 25  
**Target:** https://github.com/PCakes303/agent-skill-library  
**Visibility:** public  
**Branch:** main  
**Status:** deployed; schema parity remediation verified  
**Product files:** 20 (this status file is staging-only and is not deployed)

## Deployment evidence

- Latest product commit: https://github.com/PCakes303/agent-skill-library/commit/dbedb386c22065d1785d1de03c2a3d0ac8a36efa
- Latest product CI: https://github.com/PCakes303/agent-skill-library/actions/runs/41521270824
- CI matrix: Python 3.10, 3.11, 3.12; all jobs passed.
- Regression tests: 21 per Python version.
- Staging/product parity: all 20 product-file Git blob SHAs match.
- Workflow schema is executed by the validator and CI. Resource Manifest schema fixture is pinned to upstream commit `fec6735f895230ef41560243524aee1372f6a745`; provenance is recorded in docs/SCHEMA-PIN.md.
- No workflow execution, publisher authentication, policy enforcement or sandbox isolation is implemented.

## Scope

Experimental declarative skill package and workflow schema with a schema-backed validator, pinned canonical Resource Manifest conformance fixture, example package and security documentation. This component does not execute workflows, authenticate publishers, verify signatures, enforce policy, resolve dependencies, or provide sandbox isolation.

## Dependencies

Declared contract dependencies only: Resource Manifest, Schema Registry, Policy Engine, and Tool Adapters. No runtime integration is claimed.

## Governance

License remains pending portfolio-level review. Do not add a license file until approved. Private vulnerability reporting, GitHub About metadata and repository administration settings remain to be verified.
