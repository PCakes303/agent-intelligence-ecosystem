# Getting started

## Choose your path

### Exploring the ecosystem
1. Read this guide and the architecture overview.
2. Browse the [master registry](https://github.com/PCakes303/agent-intelligence-ecosystem).
3. Review the dependency graph before selecting a component.

### Contributing documentation or code
1. Read the target repository's README, AGENTS.md, CONTRIBUTING.md, and SECURITY.md.
2. Check its manifest, roadmap, and declared dependencies.
3. Open an issue for substantial changes.
4. Make a focused pull request with tests and evidence.
5. Update compatibility notes and changelog when contracts change.

### Building an integration
1. Identify the resource and contract versions.
2. Validate manifests and schemas.
3. Authenticate the publisher or workload using the applicable trust profile.
4. Evaluate authorization independently of discovery and authentication.
5. Add contract tests for positive, negative, and failure paths.

## Maturity labels

- **planned** — intended work, not implemented.
- **research** — investigation underway.
- **scaffolding** — repository structure and baseline documents exist.
- **experimental** — executable prototype with tests; interfaces may change.
- **alpha** — usable early release with integration and security review.
- **beta** — feature complete for the declared scope, with broader validation.
- **stable** — supported compatibility and release process.
- **maintenance** — fixes only or limited development.
- **deprecated** — migration path published.
- **archived** — no longer maintained.

A README, schema, or roadmap alone does not prove runtime capability. Look for test runs, release artifacts, compatibility reports, and provenance.

## Safe contribution checklist

- [ ] No credentials, tokens, private keys, or restricted data committed.
- [ ] Inputs and external artifacts are validated.
- [ ] Security decisions default deny and fail closed.
- [ ] Discovery and authentication are not mistaken for authorization.
- [ ] Tests include negative and failure cases.
- [ ] Requirements and dependencies are traceable.
- [ ] Claims match actual evidence.
