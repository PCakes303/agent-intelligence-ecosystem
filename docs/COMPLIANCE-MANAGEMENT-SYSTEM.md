# Compliance Management System — Charter

Status: initial governance charter, not legal advice or compliance certification. Starting location: Denver, Colorado, United States. Review date: 2026-11-02.

## Applicability
Legal applicability depends on the operating entity, developer/deployer role, users, affected persons, data categories, purposes, scale, sectors, contracts, and deployment geography. Denver is a starting jurisdiction, not the complete analysis. Each deployment must record applicable federal, Colorado, local, other-state and foreign requirements as triggered by facts.

## Registers to maintain
1. Legal obligations: jurisdiction, official source URL, exact citation, effective date, applicability conditions and rationale, status, accountable owner, last-reviewed date, counsel-review status.
2. Controls: control ID, objective, mapped obligations, implementation point, repository, owner, tests, evidence, review frequency and exceptions.
3. Data inventory: categories, source, purpose, storage, access, recipients, retention and deletion.
4. AI use cases: intended purpose, developer/deployer role, affected persons, consequential-decision context, risk assessment, human oversight, notices and contestability.
5. Evidence index: commit, CI run, test/assessment output, timestamp, retention and access classification.
6. Exceptions: risk, compensating controls, approver, expiry and remediation owner.

Keep personal data, credentials, incident evidence, confidential risk findings and legal advice in approved private systems. Publish only schemas and sanitized status.

## Initial Colorado and federal screening
This is a non-exhaustive applicability checklist, not a statement that every law applies:
- Colorado Privacy Act and implementing rules.
- Colorado data security, disposal and breach-notification statutes, including C.R.S. §§ 6-1-713, 6-1-713.5 and 6-1-716.
- Colorado SB 26-189 (Automated Decision-Making Technology), generally effective January 1, 2027; assess covered consequential decisions and developer/deployer duties.
- Colorado HB 26-1263 (Conversational AI Service Operator Requirements), effective January 1, 2027; assess covered operators, disclosures and minor safeguards.
- Colorado Anti-Discrimination Act and applicable federal civil-rights and employment laws.
- FTC Act and consumer-protection requirements.
- HIPAA, GLBA, COPPA, FERPA, FCRA and other sectoral laws only where facts trigger them.
- CFAA, ECPA/SCA, copyright, licensing, export controls, sanctions, contracts, platform and source terms as relevant.
- Other state, federal, tribal and foreign laws based on actual operations and affected persons.

Colorado's Attorney General has ongoing AI/ADMT and chatbot implementation work. Re-check enacted text, regulations, effective dates, amendments, injunctions, thresholds and exemptions before deployments. Breach notification deadlines vary by facts and legal regime; incident counsel must determine triggering events and deadlines rather than relying on a generic timer.

## Operating cycle
Inventory system/data/use case; screen jurisdictions and obligations; map each applicable obligation to an owned control; implement at the enforcement boundary; test positive, negative, abuse and failure cases; review evidence before release; monitor legal and operational changes; reassess quarterly and after material changes or incidents.

## Release gates
Block deployment when material legal applicability is unknown, required controls lack owners/evidence, privileged execution lacks emergency stop/identity/revocation/audit/isolation, required privacy or AI assessments/notices are incomplete, critical exceptions are expired, or public compliance claims cannot be substantiated.

## Official sources
- Colorado AG Privacy Act: https://coag.gov/resources/colorado-privacy-act/
- Colorado AG data protection laws: https://coag.gov/resources/data-protection-laws/
- Colorado AG AI and chatbot rulemaking: https://coag.gov/ai/
- SB 26-189: https://leg.colorado.gov/bills/sb26-189
- HB 26-1263: https://leg.colorado.gov/bills/HB26-1263
- FTC: https://www.ftc.gov/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST CSF: https://www.nist.gov/cyberframework
- NIST Privacy Framework: https://www.nist.gov/privacy-framework

Qualified counsel must validate applicability for actual operations and use cases. This charter is a governance starting point, not a complete legal inventory or certification.
