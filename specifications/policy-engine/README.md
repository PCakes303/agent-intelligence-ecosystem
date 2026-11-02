# Policy Engine — initial contract

**Status:** starter reference semantics in the master repository; dedicated repository not yet present.

The policy engine is the enforcement contract for principal/action/resource decisions across tools, skills, agents, adapters, and data access. The design is default-deny, explicit-deny-overrides, least privilege, and policy-version traceability.

## Starter
Use the existing [experimental reference evaluator](../../prototypes/policy/README.md). Run:

```bash
python tools/evaluate_policy.py --policy prototypes/policy/examples/policy.json --request prototypes/policy/examples/allow-request.json
python -m unittest discover -s tests -v
```

The evaluator is deterministic reference logic, not a production security boundary.

## Developer
Add schema-conformant policy documents, policy bundles, decision explanation codes, negative fixtures, policy versioning, and integration tests at every protected resource boundary.

## Production
Add authenticated policy distribution, signed bundles, workload identity, revocation, audit integration, rate limiting, fail-closed behavior, policy rollout/rollback, and independent security review. Never treat a policy decision as proof that the requesting principal was authenticated.
