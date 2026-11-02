# ADR 0002: Reviewed Registry Synchronization

- Status: Accepted
- Date: 2026-11-01

## Context

The ecosystem needs timely metadata synchronization without allowing arbitrary repository events or untrusted pull requests to mutate canonical control-plane data.

## Decision

Use event-driven detection followed by immutable-SHA manifest retrieval, strict schema and policy validation, dependency impact analysis, and a bot-authored pull request. Merge requires checks and human review. A scheduled reconciliation detects missed events and drift. Private repositories are excluded by allowlist and denied by default.

## Consequences

Synchronization is eventually consistent, not instantaneous. Failed validation leaves the canonical registry unchanged. Idempotency, replay protection, retry budgets, and audit provenance are required. No public workflow may access private repository content.
