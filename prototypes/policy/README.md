# Policy Decision Prototype

**Status:** experimental reference evaluator; not production authorization infrastructure.

## Contract

- Policy schema: policy.schema.json
- Request schema: request.schema.json
- Example policy: examples/policy.json
- Example request: examples/allow-request.json
- Evaluator: ../../tools/policy_engine.py
- CLI: ../../tools/evaluate_policy.py

## Semantics

The evaluator matches principal, action, resource, and required scopes. Any matching explicit deny overrides all allows. If no allow rule matches, the result is deny. Invalid policy or request data produces a deny decision.

The evaluator is intentionally small and deterministic so that default-deny and precedence semantics can be tested. It does not authenticate principals, distribute policies securely, enforce decisions at a resource boundary, or provide production-grade policy language features. Those responsibilities must be implemented and threat-modeled before deployment.

## Run

From the repository root:

```bash
python tools/evaluate_policy.py --policy prototypes/policy/examples/policy.json --request prototypes/policy/examples/allow-request.json
```
