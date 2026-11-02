# Security Policy

This repository contains a scaffolded emergency-control command schema, strict validator and deterministic reference state reducer. It is not a deployed emergency-stop service and does not authenticate commands, persist authoritative state, propagate stop signals or enforce process termination.

## Reporting

Do not publish exploitable vulnerability details, credentials, personal data or confidential incident evidence in public issues. Use GitHub private vulnerability reporting or a private security advisory only if enabled for this repository. No dedicated private reporting address is published here. If GitHub private reporting is unavailable, the owner must configure an approved private channel before production use.

## Security invariants

- Reject malformed, stale, replayed, expired and unauthenticated commands.
- Fail closed when identity, revocation, authorization, policy, state or propagation evidence is unavailable.
- STOP is not blocked by ordinary policy evaluation after command authority has been verified.
- RESUME requires two distinct verified approvers and positive policy authorization.
- A stop never expires automatically.
- Do not infer runtime enforcement from a valid command or state transition.
