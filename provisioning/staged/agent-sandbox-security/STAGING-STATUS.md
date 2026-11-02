# Agent Sandbox Security — staging status

**Portfolio repository:** 26  
**Target:** https://github.com/PCakes303/agent-sandbox-security  
**Visibility:** public  
**Branch:** main  
**Status:** deployed and verified  
**Product files:** 15 (this status file is staging-only and is not deployed)

## Scope

Experimental sandbox admission policy contract and fail-closed reference validator. It validates bounded raw JSON input (1 MiB, depth 32), at most 64 filesystem paths and 64 egress entries, path/egress string bounds, declared resource ceilings, read-only root intent, default-deny network intent, and required identity/policy/stop/artifact prerequisites. CI also checks Draft 2020-12 schema agreement for critical security boundaries. It deliberately never executes workloads.

## Security boundary

No OS isolation backend, container/namespace enforcement, filesystem/network enforcement, resource enforcement, authenticated identity integration, production policy enforcement, artifact signature verification, revocation service, or emergency-stop runtime integration is implemented. Do not use this component as a production sandbox or security boundary. Privileged execution remains prohibited.

## Portfolio dependencies

Declared contracts only: identity-trust, policy-engine, audit-provenance, secure-supply-chain, emergency-control, and compliance-governance. No runtime integration is claimed.

## Capability metadata

Capability and compatibility metadata are aligned to the ecosystem v1.1.0 contract. All upstream links remain declared/contract-only; no tested runtime integration is claimed.

## Verification plan

- Historical deployment commit: https://github.com/PCakes303/agent-sandbox-security/commit/29235a9477dafdf23ced98389c952a31fc22df3d
- Expanded regression suite: 21 tests, including pre-parse byte/depth bounds, path/egress count and length bounds, and schema/runtime security-boundary checks.
- Final remediation CI: https://github.com/PCakes303/agent-sandbox-security/actions/runs/41507530278 (verify final workflow conclusion before sign-off).
- Master staging packet refreshed with the latest validator, schema, tests, CI, requirements and security/contract docs; exact product-file parity is pending final comparison.
- Master registry, dependency graph, status and public catalog reconciled; Master regression and capability/compatibility metadata verification passed in run https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41438185138 (47 tests). Final deployment checkpoint: checkpoints/2026-11-02-agent-sandbox-security-deployment.md.

## Governance

License remains pending portfolio-level review. No license file is included.