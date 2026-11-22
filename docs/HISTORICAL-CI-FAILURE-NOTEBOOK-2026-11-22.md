# Historical CI Failure Notebook — 2026-11-22

**Purpose:** Preserve failed workflow evidence as engineering notes. Failures are observations, not blemishes to hide.  
**Scope:** Up to the 30 most recent GitHub Actions workflow runs in each of the 32 public ecosystem repositories, queried on 2026-11-22. Repositories with fewer than 30 runs returned their available history.  
**Current-state cross-check:** Latest-main workflow run succeeded in all 32 public ecosystem repositories. The master commit `52c5451c16a5d1f12cc02d83899fc4ade77b5841` had 36/36 successful check runs. Account-wide open PRs: 0.  
**Important:** This notebook records the observed failure-run counts and representative log diagnoses. It is not a claim that every historical run log was individually decoded or that no older failures exist outside the sampled window.

## Snapshot

- 32 public ecosystem repositories checked.
- 25 repositories had one or more workflow runs with a failure conclusion in the sampled history.
- 140 failed workflow runs were found in total across the sampled histories.
- These are not 140 independent defects. Many were consecutive push-triggered attempts during the same build/repair bursts, often with later attempts canceled after one matrix job failed.
- No latest-main workflow failure was observed in the 32-repository snapshot.

## Repository counts and representative evidence

| Repository | Failed runs in sampled history | Representative failure note |
|---|---:|---|
| agent-intelligence-ecosystem | 0 | No failed workflow run in sampled window; latest validation passed 36/36. |
| agent-ai-discovery | 7 | [Run 41522450391](https://github.com/PCakes303/agent-ai-discovery/actions/runs/41522450391): regression test expected a document to fail schema validation, but the validator returned no errors. Test expectation/fixture needed reconciliation with the normative schema. |
| mrcakes931-ecosystem | 0 | No failed workflow run in sampled window. |
| agent-ecosystem-integration | 4 | [Run 41523011852](https://github.com/PCakes303/agent-ecosystem-integration/actions/runs/41523011852): workflow attempted to install missing `requirements-dev.txt`. |
| agent-foundation-spec | 1 | [Run 41393874714](https://github.com/PCakes303/agent-foundation-spec/actions/runs/41393874714): starter build failed with `ModuleNotFoundError: No module named 'tools'`. |
| agent-resource-manifest | 4 | [Run 41519812898](https://github.com/PCakes303/agent-resource-manifest/actions/runs/41519812898): workflow attempted to install missing `requirements-dev.txt`. |
| agent-schema-registry | 1 | [Run 41393878459](https://github.com/PCakes303/agent-schema-registry/actions/runs/41393878459): starter build failed importing `tools.check_schema_catalog`. |
| agent-identity-trust | 6 | [Run 41519948057](https://github.com/PCakes303/agent-identity-trust/actions/runs/41519948057): regression assertion expected a previous issuer validation error, but current schema validation returned no errors for that fixture. |
| agent-secure-supply-chain | 4 | [Run 41522667863](https://github.com/PCakes303/agent-secure-supply-chain/actions/runs/41522667863): test called a missing helper, `assert_schema_reject`. |
| agent-policy-engine | 11 | [Run 41400916972](https://github.com/PCakes303/agent-policy-engine/actions/runs/41400916972): workflow invoked a nonexistent `tools/starter_build.py`. |
| agent-audit-provenance | 9 | Failure burst observed on Nov 2. Representative run logs were not decoded in this pass; current-main run is green. Preserve the historical runs for follow-up if a regression reappears. |
| aix-core | 5 | [Run 41405830545](https://github.com/PCakes303/aix-core/actions/runs/41405830545): tests invoked a missing `tools/validate_message.py` path. |
| aix-codecs | 9 | [Run 41523753842](https://github.com/PCakes303/aix-codecs/actions/runs/41523753842): test module import failed with `SyntaxError: bytes can only contain ASCII literal characters`. |
| agent-transport-gateway | 0 | No failed workflow run in sampled window. |
| agent-discovery-network | 1 | [Run 41410827524](https://github.com/PCakes303/agent-discovery-network/actions/runs/41410827524): unittest discovery reported `Start directory is not importable: 'tests'`. |
| agent-capability-registry | 3 | [Run 41520721042](https://github.com/PCakes303/agent-capability-registry/actions/runs/41520721042): workflow attempted to install missing `requirements-dev.txt`. |
| swarm-runtime | 7 | [Run 41415138593](https://github.com/PCakes303/swarm-runtime/actions/runs/41415138593): unittest discovery reported `Start directory is not importable: 'tests'`. |
| swarm-coordination | 4 | [Run 41417533500](https://github.com/PCakes303/swarm-coordination/actions/runs/41417533500): test acknowledgement lease had expired before the expected completion transition; timing/clock control required review. |
| swarm-state-mesh | 3 | [Run 41520592282](https://github.com/PCakes303/swarm-state-mesh/actions/runs/41520592282): workflow attempted to install missing `requirements-dev.txt`. |
| osint-source-registry | 0 | No failed workflow run in sampled window. |
| intelligence-knowledge-graph | 0 | No failed workflow run in sampled window. |
| agent-tool-adapters | 0 | No failed workflow run in sampled window. |
| agent-skill-library | 7 | [Run 41521123912](https://github.com/PCakes303/agent-skill-library/actions/runs/41521123912): tests expected hand-written validator error wording, but schema-first validation returned normative schema errors. Error-message assertions and test expectations needed alignment. |
| agent-sandbox-security | 9 | [Run 41507403383](https://github.com/PCakes303/agent-sandbox-security/actions/runs/41507403383): escaped-brace depth test reached a separate invalid `profile_id` check; fixture did not satisfy the full profile contract. |
| agent-emergency-control | 1 | [Run 41547347882](https://github.com/PCakes303/agent-emergency-control/actions/runs/41547347882): setup-python could not resolve a malformed version string containing a literal backslash (`\3.12`). |
| agent-compliance-governance | 12 | [Run 41550368717](https://github.com/PCakes303/agent-compliance-governance/actions/runs/41550368717): evidence-index fixture lacked required `record_status`; test expected an earlier unknown-control error, exposing validation-order/test-fixture mismatch. |
| agent-conformance-lab | 14 | [Run 41554059368](https://github.com/PCakes303/agent-conformance-lab/actions/runs/41554059368): setup-python could not resolve a malformed version string (`\3.10`). |
| osint-collection-framework | 4 | [Run 41985914086](https://github.com/PCakes303/osint-collection-framework/actions/runs/41985914086): setup-python could not resolve a malformed version string (`\3.12`). |
| osint-evidence-engine | 10 | [Run 41989245947](https://github.com/PCakes303/osint-evidence-engine/actions/runs/41989245947): Python 3.12 test step ran zero tests and exited 5; Python 3.11 job in the same run passed. Test discovery/path configuration required correction. |
| osint-entity-resolution | 1 | [Run 41991451924](https://github.com/PCakes303/osint-entity-resolution/actions/runs/41991451924): setup-python could not resolve a malformed version string (`\3.11`). |
| agent-federation-network | 0 | No failed workflow run in sampled window. |
| adaptive-swarm-compression | 3 | [Run 42020280217](https://github.com/PCakes303/adaptive-swarm-compression/actions/runs/42020280217): metadata test expected `approved-and-applied`, while the manifest correctly reported `selected`; test expectation/metadata semantics were inconsistent. |

## Failure patterns and lessons

### 1. Workflow configuration and packaging
Observed missing dependency manifests, invalid setup-python version strings, wrong script paths, and missing Python package markers/import paths. These are build-system defects, not evidence that the intended feature design is wrong.

### 2. Schema-first validation and stale test expectations
Several tests expected older hand-written validation messages or assumed a fixture was invalid when the normative schema accepted it. The correction is to align fixtures and assertions to the normative contract while preserving meaningful negative tests—not to weaken validation.

### 3. Test fixture and clock determinism
A sandbox test fixture failed a separate profile identifier requirement; a swarm acknowledgement test expired its lease before the asserted transition. Tests should isolate the behavior under test and use controlled clocks/explicit timestamps.

### 4. Test discovery
Some workflows ran zero tests or failed because the tests directory was not importable. A green job must prove tests actually ran; exit code 5 / "NO TESTS RAN" is a failure, not a pass.

### 5. Metadata/compatibility semantics
The adaptive compression failure showed a mismatch between the manifest's `selected` state and the test's `approved-and-applied` expectation. Preserve the distinction between selected, approved and actually applied.

### 6. Toolchain warning
Several historical logs included GitHub's Node.js 20 action-runtime deprecation warning. The Actions updates were subsequently integrated and the current latest-main workflows pass. Keep monitoring action runtime compatibility rather than treating a warning as a test failure.

## Current disposition

- All 32 public ecosystem repositories have a successful latest-main workflow run in the November 22 verification snapshot.
- The master commit `52c5451c16a5d1f12cc02d83899fc4ade77b5841` passed 36/36 checks.
- The 140 sampled historical failure runs remain in GitHub Actions history and are linked above. They were not deleted or rewritten.
- Current green CI does not erase historical failure evidence; the notebook preserves root-cause notes and the next prevention lesson.
- No repository is declared production-ready based on CI alone.

## Follow-up standard

If a future failure occurs, append a new dated note with exact SHA, run ID, job ID, failing step, concise log excerpt, reproduction, classification, fix, regression test, rerun link and residual risk. Do not close the corresponding engineering issue until the acceptance criterion—not just the CI step—has been met.
