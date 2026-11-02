# ADR 0001: Two-person resume authorization

- Status: accepted as the initial conservative contract; subject to explicit versioned review.
- Date: 2026-11-02

## Context

Stopping execution must be fast and must not depend on ordinary policy availability. Resuming execution is different: an attacker or compromised operator must not be able to clear a stop unilaterally.

## Decision

A RESUME command requires two distinct approvers, neither equal to the requesting actor. The trusted identity adapter must verify each approver's identity, role, signature, revocation status and authorization. The policy adapter must separately return an affirmative resume decision. The reference validator checks envelope structure only; it does not authenticate the approvers.

STOP requires a single authorized emergency-stop authority and is not subject to the resume quorum or ordinary policy veto.

## Consequences

- Resume availability is lower than stop availability by design.
- Identity and policy integrations are mandatory before operational use.
- The quorum cannot be reduced by caller configuration.
- Future changes require a new contract version and security review.
