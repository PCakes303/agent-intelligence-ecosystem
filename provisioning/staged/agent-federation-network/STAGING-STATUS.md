# Staging Status

- Portfolio registry number: 30/32.
- Canonical ID: federation-network.
- Visibility: public.
- State: partially deployed to public remote; 4 of 17 product files are present on main.
- Product files: 17 (excluding this staging record).
- Scope: local peer declaration validation only.
- CI: federation component matrix passed 12 tests on Python 3.10, 3.11 and 3.12 in [run 41518590739](https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41518590739). That run's master registry check failed because three dependency-graph edges had not yet been added; the edges were added in commit `c29c90794033a338b60dfeb27f734ec6acc904f8`. End-to-end master CI on the corrected graph is pending [run 41519030586](https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41519030586).
- License: staged mixed-license policy requires final review and deployment; no repository-level license claim until LICENSE.md is committed and provenance reviewed.
- Runtime integration, cryptographic authentication, revocation distribution, STOP propagation, remote authorization and production federation are not implemented.

- Remote tree check (2026-11-05): 4/17 product files present (`README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `SECURITY.md`); 13 product files remain.
- Remote parity: not established.
- Remote CI: not run; do not infer staging CI is remote CI.
