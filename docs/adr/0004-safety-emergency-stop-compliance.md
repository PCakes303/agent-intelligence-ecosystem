# ADR 0004: Safety, emergency stop, and compliance by design

- Status: Accepted
- Date: 2026-11-02
- Scope: All repositories, integrations, operators, and deployments
- Legal status: Engineering architecture decision, not legal advice or compliance certification

## Decision
Safety, security, emergency-stop controls, and compliance management are cross-cutting requirements and release gates. They are not optional add-ons.

### Emergency stop
The ecosystem MUST provide independently controlled, authenticated and attributable stop authority, separate from ordinary agent/task permissions. Stop scopes include task, agent, node, tenant/federation domain, and ecosystem. A stop MUST deny new privileged work, invalidate leases/capabilities, revoke or suspend credentials where applicable, quarantine affected workloads/nodes, emit durable audit evidence, and trigger independent alerting. Stop state MUST use monotonic epochs or equivalent anti-replay state. A stale resume MUST NOT override a newer stop. High-impact resumption requires separately authorized approval.

A distributed kill switch is not merely a remote button. Enforcement must exist locally at runtimes, gateways, adapters, skill execution hosts, and swarm nodes. If a node cannot validate current stop state, it MUST deny new privileged work and apply its documented safe-interruption behavior to active work. A compromised workload MUST NOT disable its own stop enforcement.

### Sandbox and execution
A valid manifest or policy decision does not prove identity, trust, safety, or isolation. No tool, skill, plugin, or agent workload may execute with privileged authority until identity, fresh authorization, artifact verification, revocation, emergency-stop enforcement, OS isolation, resource limits, network/filesystem controls, and audit are implemented and tested. Prototype validators MUST NOT be represented as sandboxes.

### Compliance management
The master repository owns the initial governance charter and obligation-to-control mapping. A dedicated agent-compliance-governance repository will own reusable registers, control catalogue, assessment workflows, evidence index, exceptions and regulatory change monitoring. Actual legal applicability analysis is deployment-specific and requires qualified counsel.

The initial jurisdiction screen is federal, Colorado, and relevant local law, with expansion for other jurisdictions triggered by operators, users, data, services, and deployment. The register must assess, as applicable, Colorado Privacy Act and rules; Colorado security/disposal/breach-notification laws; Colorado SB 26-189 automated decision-making provisions; Colorado HB 26-1263 conversational AI operator requirements; Colorado and federal anti-discrimination laws; FTC Act; sector-specific regimes such as HIPAA, GLBA, COPPA, FERPA, FCRA only where triggered; CFAA/ECPA/SCA; copyright, licensing, export controls, sanctions, contracts and platform terms.

The compliance system MUST record authoritative source, exact citation, effective date, applicability conditions/rationale, accountable owner, last review, counsel review, mapped control, implementation and evidence. It MUST track data inventories/flows, purpose and retention, privacy/security assessments, AI use cases and impact reviews, incident and breach workflows, data rights, vendors/processors, exceptions and expiry. Sensitive records and legal advice remain private.

Framework alignment (NIST AI RMF, CSF, Privacy Framework, SP 800-53/800-218, OWASP, ISO) is supporting evidence, not proof of legal compliance.

### Portfolio requirements
Every repository documents trust boundaries, data classes, permissions, threats, failure modes, audit events, emergency-stop integration, and compliance control references. CI and conformance testing cover stop propagation, stale epochs, unauthorized resume, partitions, revocation, tampering, privilege escalation, policy denial, data minimization and privacy/security failures.

## Consequences
- agent-emergency-control independently owns stop-state protocol and authority interfaces.
- agent-compliance-governance owns the compliance-management product and reusable control evidence.
- agent-sandbox-security depends on both and must fail closed when either required contract cannot be verified.
- Existing experimental components remain non-production until their own enforcement gates pass.
- Portfolio expands to 32 repositories: 31 public and 1 private. The private operations repository remains excluded from public catalog and sync.
- No legal compliance claim is permitted without current applicability analysis, documented evidence and appropriate legal review.

## Acceptance gates
1. Versioned emergency-stop state machine, trust model and threat model.
2. Tests for scope, monotonic epochs, replay, propagation, partition, local enforcement and separately authorized resume.
3. Sandbox denies execution when stop state, identity, authorization, revocation, artifact verification or isolation is missing.
4. Repository-level stop enforcement points and negative tests.
5. Source-linked obligation register, owner-assigned controls and traceable evidence.
6. Release/deployment block for unresolved critical safety, privacy, security or legal applicability gaps.
