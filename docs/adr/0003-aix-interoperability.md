# ADR 0003: AIX as an Interoperability Extension

- Status: Accepted in principle; protocol details remain research
- Date: 2026-11-01

## Context

The ecosystem requires shared task and capability semantics across heterogeneous agent protocols and transports. Existing protocols already cover important portions of agent communication and tool access.

## Decision

AIX is an extension/interoperability semantic layer. It must map to existing standards such as MCP and A2A rather than replace them. Initial experiments should use canonical JSON and JSON Schema. Binary codecs are deferred until measured need is established.

AIX candidate concepts include task intent, delegation lifecycle, acceptance/rejection, acknowledgement, status/error semantics, capability negotiation, context references, evidence/provenance references, and policy decision context. Private model reasoning and chain-of-thought are explicitly out of scope.

## Required research

Document semantic gaps, mappings, lossiness, security implications, and conformance tests before freezing a protocol. Evaluate latency, translation fidelity, authorization correctness, validation cost, and version compatibility.

## Consequences

AIX is not yet a stable protocol. The name overlaps with IBM AIX; complete naming, trademark, and discoverability review before public product branding.
