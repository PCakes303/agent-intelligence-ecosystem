# Secure Supply Chain — initial contract

This is the initial master-repository specification for the planned `agent-secure-supply-chain` project. The standalone repository has not yet been created; this contract is maintained here until it can be migrated into that repository.

## Starter scope
- Artifact identity and immutable digest metadata.
- Source repository and commit provenance.
- SBOM reference metadata.
- Explicit signature/verification status; never infer a verified signature from a digest.
- Validation of required fields and SHA-256 syntax.

## Validate the example

```bash
python tools/validate_supply_chain.py
python -m unittest discover -s tests -p "test_supply_chain.py" -v
```

The example digest is a conspicuous all-zero fixture, not a real artifact checksum. The example contains no cryptographic signature and proves no publisher identity.

## Next tiers
- Developer: generate an SBOM from a real build and bind provenance to immutable source and build inputs.
- Production: sign provenance, verify signatures against trusted identities, enforce SLSA-aligned build controls, scan dependencies, and publish tamper-evident attestations.
