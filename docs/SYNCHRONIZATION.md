# Cross-Repository Synchronization

## Objective

Keep the public ecosystem registry accurate without centralizing source-code ownership or allowing untrusted changes to rewrite canonical metadata.

## Source-of-truth model

- Each repository owns its implementation and repository-local manifest.
- The master repository owns the public portfolio index, dependency graph, ADRs, and ecosystem-level compatibility summary.
- The integration repository owns orchestration code and reusable automation contracts.
- The private repository is outside the public synchronization graph. No public workflow may fetch or export its contents.

## Event-driven flow

1. A repository change emits a repository-dispatch/webhook event or triggers a reusable workflow.
2. The integration service receives only repository identity, commit SHA, event type, and public manifest location.
3. It fetches the manifest at the immutable commit SHA, validates schema, repository identity, visibility, allowed fields, and dependency references.
4. It checks for forbidden fields and secret-like values; it rejects unknown visibility or any attempt to publish restricted metadata.
5. It computes impact against the declared dependency graph and identifies downstream contract/conformance suites.
6. It opens a bot-authored pull request to update the master registry with source repository, commit SHA, manifest digest, validation report, and impact summary.
7. Required checks run. A human reviewer approves protected registry changes; no untrusted event directly writes to the default branch.
8. After merge, downstream tests run against pinned revisions or released contract versions.
9. A periodic reconciliation job compares registry entries with each public repository's canonical manifest and detects missed events, stale commits, deleted repositories, and drift.

## Safety and reliability requirements

- Use immutable commit SHAs; never trust mutable branch names as evidence.
- Authenticate events and verify repository origin.
- Idempotency key: repository ID + commit SHA + manifest digest + event type.
- Reject stale/out-of-order updates unless a reconciliation process explicitly resolves them.
- Prevent loops by ignoring bot-generated registry-only commits as source events unless the registry schema itself changed.
- Bound retries, use dead-letter records, expose failure status, and make reprocessing safe.
- Apply least-privilege GitHub App permissions; use short-lived tokens and OIDC where available.
- Pin third-party Actions to full commit SHAs and set minimal workflow permissions.
- Keep private repository IDs and restricted metadata out of public event payloads, logs, artifacts, and dependency graph.
- Public sync must use an allowlist of public repositories and public manifest fields. Deny by default.

## Failure behavior

A failed validation does not update the canonical registry. A failed downstream test marks affected compatibility as unknown or blocked; it does not silently roll back unrelated repository changes. Reconciliation must surface drift for human resolution.

## Initial implementation sequence

1. Define and validate the repository manifest schema.
2. Add manifest validation and graph-cycle checks to master CI.
3. Define an integration event envelope and allowlist.
4. Implement manifest fetch by immutable SHA and schema validation.
5. Generate a registry-update PR with provenance metadata.
6. Add downstream contract test selection.
7. Add scheduled reconciliation and operational alerts.
8. Add security tests for forged events, replay, stale events, private data leakage, and malicious manifest content.

This document defines the target design; it does not claim the automation is already deployed.
