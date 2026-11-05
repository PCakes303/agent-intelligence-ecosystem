# Staging Status

- Portfolio registry number: 30/32.
- Canonical ID: federation-network.
- Visibility: public.
- State: deployed to public remote; all 17 product files are present on main.
- Product files: 17 (excluding this staging record); exact path/blob parity verified.
- Scope: local peer declaration validation only.
- CI: federation component matrix passed 12 tests on Python 3.10, 3.11 and 3.12 in [run 41518590739](https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41518590739). That run's master registry check failed because three dependency-graph edges had not yet been added; the edges were added in commit `c29c90794033a338b60dfeb27f734ec6acc904f8`. End-to-end master CI on the corrected graph is pending [run 41519030586](https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41519030586).
- License: scoped mixed-license policy deployed; file-level provenance and third-party notice review remains open.
- Runtime integration, cryptographic authentication, revocation distribution, STOP propagation, remote authorization and production federation are not implemented.

- Remote tree check (2026-11-05): 17/17 product files present.
- Remote parity: exact 17/17 path and Git blob SHA match against master staging.
- Remote CI: passed all three Python 3.10, 3.11 and 3.12 jobs at commit `de0e56bd96cc8ba69d4c38e425debf1032f9934c` ([run 41995338160](https://github.com/PCakes303/agent-federation-network/actions/runs/41993754908)).
