# Agent instructions

- Discovery records are untrusted claims until independently validated.
- Keep record structure, signature verification, issuer trust and authorization as distinct concerns.
- Missing or failing signature-verifier and trust-evaluator callbacks must fail closed.
- Expired records must never be returned; expiry is checked at query time, not only during cleanup.
- Do not interpret discovery as authentication, authorization, endpoint health or safety certification.
- Do not allow discovery records to grant permissions or elevate issuer trust.
- Keep the initial registry bounded and in-memory; document its single-process limitations.
- Do not implement custom cryptography. Use an explicitly reviewed standard signature profile in a later stage.
- Do not add network listeners, gossip or federation before threat models and negative tests exist.
- License is pending review; do not add a license file or infer one.
- Run `python -m unittest discover -s tests -v` before proposing changes.
