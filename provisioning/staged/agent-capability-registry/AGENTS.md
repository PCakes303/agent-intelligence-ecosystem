# Agent instructions

- Keep capability declarations bounded and treat them as untrusted claims, not proof of behavior or trust.
- Validate identifiers, descriptions, semantic versions and attribute mappings against the canonical capability contract.
- The local registry must remain bounded; match requests must not exceed the configured requirement limit.
- Snapshot registered attributes into immutable mappings so caller-side mutation cannot change validated state.
- Policy callbacks are integration seams; only explicit boolean `True` may admit a candidate. Missing, false, non-boolean or raising callbacks deny.
- Matching is advisory only; never authenticate, authorize protected actions, execute work, or certify capabilities from a registry match.
- Do not implement custom cryptography. Signed attestations and identity lifecycle require separately reviewed standards and integrations.
- Keep dependencies declared until reproducible cross-repository conformance tests pass.
- License is pending review; do not add a license file or infer one.
- Run `python -m unittest discover -s tests -v` before proposing changes.
