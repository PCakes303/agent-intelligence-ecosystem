# Emergency Command Contract v1.0

## Command lifecycle

A command is a short-lived, signed request. Its expiry bounds command acceptance only; it does not expire an active stop. Every scope has an independent monotonic epoch. A command with an epoch less than or equal to the current scope epoch is stale or replayed.

### STOP

1. Strictly parse and validate the command.
2. Verify the signature, issuing principal's emergency-stop authority, freshness and revocation status through a trusted identity adapter.
3. Commit the active stop state durably before relying on downstream consumers.
4. Append an attributable audit event and propagate the stop to every registered enforcement point.
5. Require consumer acknowledgements and fail closed at consumers when stop state cannot be verified.

Ordinary policy evaluation must not veto a correctly authenticated STOP. A STOP command must not be delayed by a resume-only quorum.

### RESUME

1. Require an active stop for the exact same scope.
2. Require a strictly higher epoch and a fresh, signed command.
3. Require two distinct approvers, neither equal to the requesting actor; identity and role claims must be verified independently.
4. Require a positive resume-policy decision.
5. Record resume intent and evidence, coordinate a prepare/commit protocol with enforcement points, and release the stop only after the authoritative state transition and required acknowledgements are committed.

The two-approver quorum is the initial conservative contract. A future policy revision must be explicit, versioned and reviewed; no caller may silently reduce it.

## Trusted boundary

The reference reducer accepts a CommandVerifier protocol and requires explicit positive evidence for signature validity, actor authority, revocation clearance and freshness. RESUME additionally requires verified quorum and policy evidence. The adapter is responsible for cryptographic verification and trustworthy evidence. The reference package does not implement that adapter.

## State semantics

- STOP is monotonic for the selected scope and epoch.
- A newer STOP may reassert the same scope.
- RESUME cannot clear a missing stop, a different scope or a stale epoch.
- An active stop for one scope cannot be overwritten by a command for another scope.
- Stop state never auto-clears on command expiry, process restart or connectivity loss.
- A missing, malformed or stale stop-state record must be interpreted as stop active / execution denied by every future enforcement adapter.

## Current implementation limit

This repository implements strict command parsing and a pure transition reducer only. Durable compare-and-swap storage, audit integration, cryptographic verification, revocation, distributed prepare/commit, acknowledgements, quarantine and enforcement are design requirements, not implemented capabilities.
