# Staging Checkpoint — agent-compliance-governance — 2026-11-02

**Portfolio registry ID:** compliance-governance  
**Canonical registry position:** 29 of 32 (component sequence number 28; master is position 1)  
**Target remote:** https://github.com/PCakes303/agent-compliance-governance  
**Remote existence:** not created; repository-creation action is unavailable in this session  
**Staging path:** \`provisioning/staged/agent-compliance-governance/\`  
**Product files:** 28 (administrative STAGING-STATUS.md excluded)  
**Staging source commit:** \`5ba7d674727a828c9440d9599f711bf730a2d471\`  
**Master workflow:** [run 41513079895](https://github.com/PCakes303/agent-intelligence-ecosystem/actions/runs/41513079895) — success  
**Matrix:** Python 3.10, 3.11 and 3.12; 10 tests passed in each matrix job; registry validator passed; master 47-test suite and starter build passed.  
**Disposition:** STAGED; not a remote component audit, legal opinion or compliance acceptance.

## Delivered scaffold

- Six source-linked Colorado monitoring records: Colorado Privacy Act, SB26-189, HB26-1263, proposed ADMT/Chatbot rules, xAI v. Weiser litigation monitor and NIST AI RMF 1.0 voluntary guidance.
- Eleven proposed governance controls covering inventory, applicability, regulatory monitoring, privacy data mapping/rights/sensitive processing, AI risk/human oversight, transparency, ADMT records, chatbot safeguards and evidence provenance.
- Three Draft 2020-12 schemas for legal register, control catalogue and evidence index.
- Strict bounded JSON loader rejects duplicate keys, non-standard numeric constants, documents above 2 MiB and nesting above 32 levels.
- Registry validator checks schema shape, date ordering, duplicate IDs and cross-references.
- Evidence index intentionally contains zero records; no evidence is fabricated.
- Python 3.10–3.12 CI matrix passes 10 tests per interpreter.

## Legal status and limits

This repository is not legal advice, a legal applicability determination, a compliance officer, an audit opinion or a certification. The Colorado sources are an initial monitoring baseline because the ecosystem owner is based in Denver; location alone does not establish applicability. Counsel must review entity role, processing activity, user population, thresholds, sector, exemptions, effective dates, proposed rules and litigation status.

The Colorado Attorney General states that SB26-189 and HB26-1263 take effect January 1, 2027. The Colorado Privacy Act has been in effect since July 1, 2023, subject to statutory thresholds and exemptions. Proposed ADMT/Chatbot rules and the xAI v. Weiser stay are separately recorded and must not be conflated with enacted statutes or treated as exemptions. See \`docs/LEGAL-REGISTER.md\` and the source URLs in \`registry/legal-applicability.json\`.

All eleven controls remain proposed; none is marked implemented or evidenced. NIST AI RMF is recorded as voluntary guidance, not binding law by itself.

## Next steps

1. Owner creates public repository \`PCakes303/agent-compliance-governance\`.
2. Push the 28 product files; do not copy the administrative staging record as product content.
3. Run the repository's own CI matrix and verify exact remote/staging Git blob parity.
4. Obtain counsel review for each legal record and the actual business/system facts; update applicability only with a named reviewer and evidence.
5. Establish private evidence storage, named control owners and regulatory monitoring operations before production use.
