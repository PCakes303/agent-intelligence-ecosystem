# Agent instructions

- Treat every command, signature, identity, timestamp, scope and approval as untrusted until verified by an explicitly trusted adapter.
- Never implement a permissive fallback when a verifier, state store, audit sink, revocation source or propagation service is unavailable.
- STOP must remain fail-closed and must not be vetoed by ordinary policy evaluation.
- RESUME must require two distinct independently authenticated approvers and a positive policy decision.
- Never auto-clear a stop because a command or lease expires.
- Do not add network, process, container, filesystem or operating-system enforcement to this reference package.
- Do not describe schemas, tests or reducer logic as a deployed kill switch.
- Add replay, stale epoch, scope-confusion, verifier failure and partial-propagation tests for integration work.
- Keep secrets, live credentials, real incident details and personal data out of this public repository.
- Run python -m unittest discover -s tests -v before committing.
