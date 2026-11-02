# Security Policy

## Reporting

Do not publish exploitable vulnerabilities in public issues. Use GitHub private vulnerability reporting or a private security advisory if enabled for this repository. A dedicated private reporting address is not published here; if private reporting is unavailable, the owner must configure a private reporting channel before production use. Do not send exploit details, credentials, tokens, or sensitive event data through public channels.

## Scope and limitations

This scaffold implements event-shape checks and a SHA-256 hash chain. It does not authenticate event producers, prove event truth, provide trusted timestamps, protect a log against truncation without an external checkpoint, or implement digital signatures.

Never include secrets, credentials, tokens, or unnecessary personal data in events. Treat logs as potentially sensitive operational records even when examples are public.
