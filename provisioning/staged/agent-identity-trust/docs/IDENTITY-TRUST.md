# Identity and trust contract

A principal identifier names an entity within an issuer's namespace. It is not, by itself, authentication, authorization, or proof of human ownership.

## Requirements
- Authenticate principals using verifiable credentials or established identity protocols.
- Bind credentials to issuer, audience, validity interval, and intended use.
- Authorize each action against explicit policy; default to deny.
- Scope delegation by action, resource, audience, and expiry.
- Support revocation and key rotation; cache validity only for bounded periods.
- Record security-relevant decisions without logging secrets.

SPIFFE/SPIRE, OAuth 2.0, and OpenID Connect are integration targets. This repository currently defines data contracts only; it does not issue credentials or operate an identity provider.
