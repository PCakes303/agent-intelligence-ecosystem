# SBOM Policy

## Starter
An SBOM is a machine-readable inventory of components used to build or distribute an artifact. Use SPDX or CycloneDX. Record the exact artifact digest to which the SBOM applies, the generator and version, generation time, and source/build identity.

The starter example references an SBOM URI but does not fetch or validate the referenced document. Never infer completeness or authenticity from the presence of a URI.

## Developer
- Generate an SBOM from the actual build output, not from a manually curated dependency list alone.
- Include direct and transitive dependencies where tooling supports them.
- Record package identifiers, versions, dependency relationships, licenses, and known omissions.
- Compare the SBOM against lockfiles and build inputs.
- Keep generated SBOMs immutable and bind them to the release digest.

## Production
- Publish SPDX or CycloneDX documents alongside each release.
- Sign or attest the SBOM and bind it to the artifact digest.
- Scan for known vulnerabilities and license-policy violations.
- Define update cadence, retention, exception expiry, and disclosure handling.
- Do not claim an SBOM proves an artifact is safe or vulnerability-free.
