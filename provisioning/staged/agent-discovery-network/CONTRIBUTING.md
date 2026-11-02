# Contributing

Changes to discovery records, trust filtering or expiry semantics require a contract update, threat-model review and positive/negative tests.

Before submitting:
1. Read `AGENTS.md`, `SECURITY.md` and `docs/DISCOVERY-CONTRACT.md`.
2. Test expired, malformed, replayed, unverified and untrusted records.
3. Ensure callback failures deny rather than allow.
4. Document whether trust decisions come from a real Identity & Trust integration or a test double.
5. Run `python -m unittest discover -s tests -v`.

Never commit credentials, private keys, tokens or private operational material. Do not claim cryptographic or distributed security without reproducible evidence.
