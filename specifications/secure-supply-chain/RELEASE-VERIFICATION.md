# Release Verification

Before accepting a release, a consumer should:

1. Obtain the artifact from an approved distribution channel.
2. Compute its digest locally and compare it with the published digest.
3. Obtain the SBOM and provenance by immutable reference.
4. Verify signature/attestation cryptographically against the configured trust policy.
5. Confirm source repository, commit, workflow, builder, and artifact digest agree.
6. Evaluate dependency and vulnerability policy.
7. Record the decision, evidence references, policy version, and timestamp.

A failed or unavailable verification must not silently downgrade to trust. The consumer may reject or quarantine the artifact. This repository's starter validator checks record shape only; it does not perform cryptographic verification, download artifacts, or scan vulnerabilities.
