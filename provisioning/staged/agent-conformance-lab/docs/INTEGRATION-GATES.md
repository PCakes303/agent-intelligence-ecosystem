# Integration Gates Before Claiming Interoperability

1. Pin every subject and dependency repository commit and schema version.
2. Validate actual manifest/capability/compatibility artifacts from the pinned revisions.
3. Run positive, negative and boundary protocol fixtures across producer and consumer implementations.
4. Test identity authentication, authorization, revocation and stale credential behavior.
5. Test policy allow/deny, scope mismatch and policy-service outage.
6. Test audit event integrity and failure handling.
7. Test emergency STOP, propagation, acknowledgement, stale epoch rejection and two-person RESUME.
8. Test compliance controls and counsel-reviewed applicability for the use case.
9. Verify signed supply-chain provenance and artifact digests.
10. Verify OS-level sandbox, filesystem, network, process and resource boundaries for privileged workloads.
11. Record reproducible evidence, runner identity, environment, timestamps and limitations.
12. Keep any untested or unavailable integration gate BLOCKED.

A local JSON schema fixture is not proof of cross-repository runtime interoperability.
