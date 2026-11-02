# Foundation Starter Path

This is the first learning path through the ecosystem's security and governance foundations.

## Build order

1. **Foundation Spec:** understand requirement IDs, invariants, and acceptance criteria.
2. **Schema Registry:** read and validate JSON Schema 2020-12 contracts.
3. **Resource Manifest:** describe a tool/resource without executing it.
4. **Identity Trust:** distinguish an identity record from authentication and authorization.
5. **Policy Engine:** run the default-deny evaluator and test deny-overrides.
6. **Audit Provenance:** validate an event and understand the limits of hash chains.
7. **Secure Supply Chain:** bind source, artifact digest, SBOM, and provenance evidence.

## Learning outcomes

A beginner should be able to clone the repository, install its development requirements, run the starter build, inspect one example, intentionally break one field and observe validation fail, then add a test for the new behavior.

## Safety boundaries

Starter examples are fixtures, not production credentials, real signatures, real attestations, or verified artifacts. Never insert secrets or personal data into public fixtures. No starter build should execute an untrusted tool or grant it permissions.
