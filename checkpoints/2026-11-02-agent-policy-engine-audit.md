# Component Audit — agent-policy-engine — 2026-11-02

**Repository:** [PCakes303/agent-policy-engine](https://github.com/PCakes303/agent-policy-engine)  
**Audited implementation commit:** `39ead9528a149b1511cfb69b1c996d5e77c6ff64`  
**Baseline CI:** [Run 41400923896](https://github.com/PCakes303/agent-policy-engine/actions/runs/41400923896) — success  
**Remediation commits:** `6a78a880bd66762d8e32177b8723b0ff2a2a2d9f`, `bdd569b3d2af701d0b0f0cb1a0647bd04875b996`  
**Remediation CI:** [Run 41490159810](https://github.com/PCakes303/agent-policy-engine/actions/runs/41490159810) — success (starter build, nine unit tests and CLI example passed)  
**Disposition:** **BLOCKED**  
**Maturity:** Experimental local policy decision evaluator; not a production authorization enforcement boundary.

## Verified implementation

- Draft 2020-12 schemas define policy bundles and decision requests, including bounded fields/collections and rejection of unknown properties.
- The evaluator uses `jsonschema.Draft202012Validator` against both schemas before evaluation.
- Evaluation is deterministic and side-effect free: explicit deny overrides allow, matching allow returns allow only when no deny matches, and no matching allow returns default deny. Invalid policy/request input returns a deny result.
- Wildcard matching uses Python `fnmatch.fnmatchcase`, explicitly documented in the contract; consumers must not interpret it as regular expressions or shell expansion.
- CLI accepts local policy/request JSON files and exits 0 only for allow; the code does not retrieve policies over a network or execute policy text.
- Nine unit tests cover allow, unknown principal, missing scope, deny precedence, restricted resource, invalid request, non-object policy, invalid scopes and enforced default-deny policy.
- Starter build runs the full unit suite and CLI example. CI installs pinned `jsonschema==4.25.1` and runs the starter build. Baseline run 41400923896 succeeded.
- README, threat model and capabilities explicitly disclaim principal authentication, signed distribution, protected-resource enforcement, revocation, production hardening and compliance certification.
- License metadata is pending review; no license was added.

## Corrections committed during audit

- `6a78a880bd66762d8e32177b8723b0ff2a2a2d9f`: removed stale `09 / 29` portfolio-position text and added explicit pending-license disclosure to README.
- `bdd569b3d2af701d0b0f0cb1a0647bd04875b996`: replaced obsolete empty-remote creation instructions in `STAGING-STATUS.md` with a deployment record and outstanding staging-parity requirement.
- Created [issue #1](https://github.com/PCakes303/agent-policy-engine/issues/1) for malformed About description, private reporting verification and repository settings review.

## Findings and remaining exceptions

1. **Private reporting route unverified:** SECURITY.md points to GitHub private vulnerability reporting only if enabled; manifest `security_contact` is null. Verify the feature is enabled or configure an owner-approved private route before production use.
2. **GitHub About metadata malformed:** live description has topic keywords appended to descriptive prose; homepage and topics are empty. The master metadata guide is only a proposal. Apply and verify the actual GitHub About fields separately.
3. **License pending:** no root `LICENSE` file or GitHub license declaration was observed. README now explicitly states that reuse and redistribution rights must not be assumed.
4. **Staging parity outstanding:** historical staging-to-remote blob SHA parity must be refreshed against current `main` before portfolio-wide sign-off.
5. **Administration controls unverified:** branch rulesets/protection, Actions permissions, secret scanning, push protection and dependency alerts were not confirmed through the available integration.
6. **No enforcement integration:** no adapter forces protected resources to enforce decisions. An allow result is not proof of identity and must not be trusted without independent authentication and resource-boundary enforcement.
7. **Policy trust lifecycle absent:** no signed policy distribution, cryptographic policy verification, trusted policy update channel, freshness controls or revocation-aware identity integration is implemented.

## Acceptance to clear BLOCKED

- Verify a private vulnerability reporting route.
- Correct the GitHub About description and apply relevant topics/homepage; verify the live metadata.
- Complete repository administration checks and staging parity.
- Retain the pending license decision until explicitly approved.
- Before production authorization use, implement independently authenticated identity binding, signed/fresh policy distribution, protected-resource enforcement, revocation handling, audit integration and independent security review.

A passing starter CI run validates this experimental local evaluator and nine tests. It does not certify identity, policy authenticity, deployment enforcement, legal compliance or production security.
