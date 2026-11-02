# Security policy

This repository begins as an in-memory discovery index and callback-based trust-filtering scaffold. It is not a production discovery service.

Discovery records are untrusted input. The initial code validates shape, timestamps, endpoint scheme and expiry, then requires caller-supplied signature-verification and issuer-trust callbacks. Those callbacks are integration seams; they are not cryptographic implementations or a connection to the production Identity & Trust service.

A record being returned means only that it passed the configured local filters at query time. It does not prove that the endpoint is reachable, that its current operator controls the endpoint, that its advertised capabilities are real, or that any action is authorized.

Production deployment requires a reviewed signature profile, authenticated issuer/key lifecycle, revocation handling, policy-bound visibility, transport authentication, bounded distributed storage, rate limits, abuse controls and adversarial testing.

Report suspected vulnerabilities privately to the maintainer. Do not publish exploit details or secrets in public issues.
