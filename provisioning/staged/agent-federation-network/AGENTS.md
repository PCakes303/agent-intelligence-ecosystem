# Agent Instructions

- Treat all peer metadata and remote claims as untrusted input.
- Never infer authentication, authorization or trust from a URL, DNS, repository, signature field, or discovery listing.
- Preserve independent domain ownership and explicit trust scopes.
- Default to deny. Revocation, expired trust, policy uncertainty, or emergency STOP means no federation.
- Never implement arbitrary remote execution, credential forwarding, or implicit trust transitivity.
- Do not collect or process personal data in this scaffold.
- Keep capabilities and compatibility claims evidence-backed; no production or certification claims.
