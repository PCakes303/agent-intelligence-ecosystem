# Agent instructions

- Treat all event content as untrusted input.
- Never claim a hash chain is a digital signature or proof that an event is true.
- Preserve fail-closed validation and deterministic canonicalization.
- Do not log secrets, credentials, access tokens, or unnecessary personal data.
- Keep examples synthetic.
- Run `python tools/starter_build.py` and the complete unittest suite before proposing changes.
- Any schema or hash-format change requires a versioned compatibility decision.
