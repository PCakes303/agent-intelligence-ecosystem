# Provenance and Attestations

## Starter
Record source repository, immutable commit, artifact digest, SBOM reference, and explicit signature state. The sample record is illustrative and is not cryptographically signed.

## Developer
Capture build identity, builder identity, build invocation, resolved dependencies, and materials. Prefer established in-toto/SLSA provenance structures and Sigstore tooling rather than inventing a custom signing protocol.

## Production
- Verify signatures and attestations against an explicit trust policy.
- Bind trusted issuer, repository, workflow, ref, and builder identity.
- Reject mutable tags as sole provenance references.
- Enforce separation between build, sign, and publish permissions.
- Use short-lived OIDC identities where available; avoid long-lived signing secrets.
- Preserve verification results and policy version in audit records.

A digest establishes byte identity only. A signature establishes a cryptographic relationship to a key or identity only when verified under a trustworthy key/identity policy. Neither alone proves source correctness or build safety.
