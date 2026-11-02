# Threat Model

## Assets

- Accurate legal-source metadata and effective-date history.
- Correct distinction between law, proposed rule, court order and voluntary guidance.
- Confidentiality and integrity of evidence records.
- Traceable control ownership, review and approval.
- Correct legal applicability decisions made by qualified reviewers.

## Threats and controls

| Threat | Reference control | Remaining requirement |
|---|---|---|
| Stale or superseded legal source | Source URL, last-verified and next-review fields | Active source monitoring and counsel review |
| Incorrect applicability conclusion | Records remain unassessed or needs-counsel | Entity-specific legal analysis |
| Draft rule represented as binding | Separate proposed status | Monitor adoption and effective dates |
| Court stay misread as exemption | Litigation monitor and explicit uncertainty | PACER review and counsel interpretation |
| Fake compliance evidence | Evidence metadata and digest format validation | Trusted storage, signatures, access control and independent review |
| Sensitive data leakage | Public evidence index policy and access classes | Private evidence vault and retention controls |
| Control status inflation | Explicit lifecycle states | Named owner, test scope and objective evidence |
| Regulatory change missed | Next-review dates and monitor controls | Scheduled monitoring, alerting and escalation service |

## Non-goals

This scaffold does not provide legal advice, legal research automation, compliance certification, an evidence vault, privacy request handling, security controls enforcement or a regulatory alert service.
