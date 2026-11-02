# AIX Core — interoperability contract

**Status:** experimental specification in the master repository. AIX is an extension/interoperability layer, not a replacement for MCP, A2A, HTTP, OpenAPI, or existing agent protocols.

## Scope
AIX defines a common semantic envelope for:
- task intent, objective, constraints, and lifecycle;
- acceptance, rejection, acknowledgement, status, result, and error;
- capability requirements and negotiation;
- context and evidence references;
- idempotency, deadlines, correlation, and causation;
- authentication context and authorization-decision references;
- source protocol and mapping provenance.

The current experimental JSON Schema is [here](../../prototypes/aix/aix-message.schema.json), with a [task request fixture](../../prototypes/aix/examples/task-request.json).

## Explicit non-goals
AIX does not authenticate a sender, authorize access, provide transport security, define a model's private reasoning, guarantee exactly-once execution, or replace the source protocol's semantics. It must not serialize chain-of-thought or hidden reasoning.

## Starter
Install the master repository's development requirements, then run:

```bash
python tools/validate_aix_message.py
python -m unittest discover -s tests -p "test_aix_contract.py" -v
```

## Developer
Add lifecycle message fixtures, MCP/A2A mapping examples, compatibility tests, duplicate/replay tests, and property-based validation.

## Production
Only after interoperability evidence: versioned conformance profiles, signed schema releases, transport binding, identity/policy integration, observability, fuzzing, compatibility guarantees, and independent security review.
