# Ecosystem architecture

## Overview

The MrCakes931 Agent Intelligence Ecosystem is a coordinated portfolio of 32 repositories (31 public and one private operations repository). It is designed as a composable system of specifications, schemas, identity and security contracts, protocols, distributed-agent infrastructure, intelligence workflows, and adoption tooling.

The architecture uses a **hybrid swarm model**: a shared control plane publishes canonical metadata and policy contracts, while independently operated nodes and federated domains retain operational autonomy. Peer-to-peer exchange may be used where appropriate, but trust boundaries remain explicit.

## Architectural layers

1. **Control plane** — the master repository owns the public repository registry, dependency graph, governance, ADRs, and compatibility overview.
2. **Ecosystem entrypoints** — discovery metadata and this human guide make the ecosystem navigable.
3. **Foundation and cybersecurity** — common vocabulary, schemas, manifests, identity, authorization, audit, and supply-chain integrity.
4. **Protocols** — AIX provides an extension/interoperability semantic layer over existing protocols; codecs and transport adapters handle representation and delivery.
5. **Swarm** — discovery, capability catalogues, runtime, coordination, and state synchronization.
6. **Intelligence** — source catalogues, authorized collection, evidence preservation, entity resolution, and knowledge graph.
7. **Adoption and federation** — tool adapters, reusable skills, sandboxing, conformance testing, and independent network federation.
8. **Private operations** — a separate private repository for restricted planning and operational material; it is excluded from public exports.

## Trust boundaries

- Discovery is not trust.
- A manifest describes a resource; it does not authorize use.
- Authentication identifies a principal; it does not authorize an action.
- Authorization is evaluated for a principal, action, resource, context, and policy version.
- Enforcement occurs at the protected resource boundary.
- Audit integrity is not proof of truth or completeness.
- A signature binds a key to bytes; it does not prove the publisher is safe.
- Public repositories must never receive private operational data through synchronization.

## Interoperability strategy

Reuse established standards by composition. Candidate mappings include MCP for tool/resource interfaces, A2A for agent task exchange, JSON Schema for data contracts, OIDC and SPIFFE/SPIRE for identity profiles, OPA for policy, Sigstore and SLSA for supply-chain integrity, and OpenTelemetry for observability. Adoption requires an ADR and compatibility evidence.

AIX is an extension layer, not a replacement for MCP, A2A, or existing transport standards. It must demonstrate semantic value and measure translation loss, latency, validation cost, and authorization correctness.

## Delivery principles

- Each repository is authoritative for its own implementation.
- The master registry is authoritative for ecosystem-wide identity and dependency metadata.
- Dependency edges describe contracts, not vendored source.
- Breaking changes require explicit versioning and migration guidance.
- Planned capabilities are never represented as implemented.
- Every maturity promotion requires reproducible tests and evidence.
