# Entry-level build

Requires Python 3.10+; no third-party packages are required.

```bash
python tools/starter_build.py
python -m unittest discover -s tests -v
```

The starter build validates the illustrative principal record's shape, issuer URI, timestamp, principal type, and status. It deliberately does not authenticate the principal or issue credentials.

**Next tiers**
- Developer: add issuer-specific credential verification and negative test fixtures.
- Production: integrate workload identity, key rotation, audience restrictions, revocation, delegated authorization, and auditable policy decisions.
