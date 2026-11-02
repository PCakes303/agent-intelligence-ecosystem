# AI Discoverability and Agent Integration Standard

**Status:** Draft ecosystem standard  
**Scope:** All 29 public repositories; private repository excluded from public discovery  
**Authority:** Master repository registry and repository-local implementation evidence

## 1. Objective

Make every public project understandable and safely consumable by AI coding agents, research agents, search/indexing systems, and agent runtimes. Discovery must be machine-readable, evidence-backed, and explicit about maturity and security boundaries.

Discoverability is not registration with every model provider and does not guarantee indexing, retrieval, recommendation, or execution.

## 2. Standard entry-point set

Every public repository should progressively provide:

| File | Purpose | Requirement |
|---|---|---|
| `README.md` | Human overview and quick start | Required |
| `AGENTS.md` | Instructions for coding agents | Required |
| `llms.txt` | Concise LLM-oriented site/repository map | Required |
| `llms-full.txt` | Expanded curated technical context | Recommended when content is substantial |
| `manifest.json` | Canonical repository identity, version, status, interfaces, dependencies, license state | Required; schema governed centrally |
| `capabilities.json` | Capability inventory with status and evidence | Required |
| `compatibility.json` | Declared and tested compatibility, clearly distinguished | Required |
| `agent-card.json` | A2A Agent Card only when a real deployed A2A endpoint exists | Conditional; never fabricate an endpoint |
| `mcp_server.py` | MCP server only when real, useful, permission-safe tools/resources exist | Conditional; no empty or decorative server |
| `schemas/` | JSON Schemas for published machine contracts | Required where machine contracts exist |
| `examples/` | Valid examples and negative examples | Required where contracts exist |

Each repository's README should link these entry points near the top. `llms.txt` must link canonical source files, not duplicate large documents that drift.

## 3. Metadata quality

Every capability record must contain:
- stable capability ID;
- concise name and description;
- lifecycle status: `proposed`, `planned`, `scaffolded`, `experimental`, `implemented`, `tested`, or `released`;
- machine-readable input/output or interface references when applicable;
- evidence links for tested/released claims;
- explicit limitations and non-capabilities.

Do not use a single repository-level status to imply every capability has the same maturity. Do not claim "MCP compatible", "A2A compatible", "secure", or "production ready" merely because a file exists.

## 4. MCP policy

MCP is the tool/resource integration surface, not a marketing badge. Implement `mcp_server.py` only when the repository can expose concrete, deterministic functions or resources.

Initial ecosystem MCP design:
- transport: stdio for local developer/agent use;
- read-only resources first: public repository registry, dependency graph, public schemas, capability records, compatibility records, and documentation;
- tools: deterministic validation or lookup functions only, with strict input validation and bounded output;
- no arbitrary shell, filesystem traversal, network proxy, credential access, private repository access, or implicit write operations;
- writes, if ever introduced, require explicit authorization, scoped credentials, policy enforcement, audit events, and negative tests;
- declare server version, MCP SDK version, supported protocol version, installation steps, and tool schemas;
- add integration tests using an MCP client and verify the actual server handshake and tool invocation.

The master repository is the natural first MCP host after its public registry and validators have stable, testable interfaces. Until then, publish this design and do not advertise a functioning server.

## 5. A2A Agent Card policy

An A2A Agent Card describes a deployed agent service and its actual endpoint/capabilities. It is not interchangeable with a repository manifest or a static project profile.

Publish a standard `/.well-known/agent-card.json` only when:
- a service endpoint is deployed and reachable;
- the card's URL, version, skills, input/output modes, and authentication requirements match reality;
- security and capability claims have evidence;
- the endpoint has an owner and operational lifecycle.

For repositories that are specifications, schemas, libraries, or documentation without a running agent service, use `manifest.json`, `capabilities.json`, and `llms.txt`; do not fabricate an A2A URL.

## 6. Repository role profiles

| Repository | Agent-facing emphasis | Initial useful surface |
|---|---|---|
| agent-intelligence-ecosystem | Portfolio discovery and governance | Registry, graph, status, public schema lookup |
| agent-ai-discovery | Discovery records and index generation | Search/list/validate discovery metadata |
| mrcakes931-ecosystem | Onboarding and navigation | Curated docs and task-oriented learning paths |
| agent-ecosystem-integration | Interoperability recipes | Protocol mapping fixtures and compatibility lookup |
| agent-foundation-spec | Normative constraints | Requirement lookup and traceability matrix |
| agent-resource-manifest | Resource declarations | Schema validation and manifest inspection |
| agent-schema-registry | Schema discovery | Schema index, version lookup, compatibility checks |
| agent-identity-trust | Identity/trust contracts | Schema and lifecycle documentation; no trust decisions without a real enforcement service |
| agent-secure-supply-chain | Artifact integrity | SBOM/provenance verification only when implemented |
| agent-policy-engine | Policy evaluation | Policy validation/evaluation with explicit policy inputs |
| agent-audit-provenance | Event integrity | Event validation and chain inspection; no truth guarantee |
| aix-core | AIX semantics | Contract lookup and message validation |
| aix-codecs | Encoding/decoding | Deterministic codec tools and test vectors |
| agent-transport-gateway | Transport interoperability | Protocol adapter status and safe test endpoints |
| agent-discovery-network | Distributed discovery | Peer discovery contracts and test harness |
| agent-capability-registry | Capability catalog | Capability search and manifest validation |
| swarm-runtime | Agent execution lifecycle | Runtime status and constrained task submission only when deployed |
| swarm-coordination | Coordination | Plan/assignment inspection and simulation |
| swarm-state-mesh | Shared state | State schema and consistency test tools |
| osint-source-registry | Source catalog | Public source metadata and reliability labels |
| osint-collection-framework | Collection workflows | Policy-bounded collection templates; no unrestricted scraping |
| osint-evidence-engine | Evidence handling | Provenance and evidence validation |
| osint-entity-resolution | Entity resolution | Explainable matching with confidence and source traceability |
| intelligence-knowledge-graph | Knowledge graph | Query schema and provenance-aware graph lookup |
| agent-tool-adapters | Tool integrations | Adapter catalog and contract tests |
| agent-skill-library | Skills | Skill manifests and safe usage instructions |
| agent-sandbox-security | Isolation | Sandbox policy validation and test harness |
| agent-conformance-lab | Conformance | Run conformance suites against supplied artifacts |
| agent-federation-network | Federation | Federation metadata and trust-boundary inspection |
| agent-ecosystem-private | Private operations | Excluded from all public indexes and public agent entry points |

## 7. Consistency and validation gates

A future `tools/validate_agent_discoverability.py` should check:
1. required files exist in every public repository;
2. JSON parses and validates against centrally versioned schemas;
3. repository IDs, names, URLs, visibility, and status agree with the master registry;
4. links resolve to files in the correct repository;
5. capabilities marked tested/released include evidence;
6. declared compatibility is not confused with tested compatibility;
7. no public metadata points to private paths, secrets, or unapproved endpoints;
8. A2A cards have a real endpoint and valid standard fields;
9. MCP server claims are backed by runnable server tests and a client handshake;
10. `llms.txt` is concise, current, and links authoritative sources.

## 8. Rollout

1. Master control plane: establish the standard, central index, and agent instructions.
2. Existing seven component repositories: reconcile metadata and add consistent `llms.txt`; refine `AGENTS.md` and manifests.
3. First useful MCP implementation: master read-only registry/schema/validator server after stable API tests.
4. New repositories: apply a standard template before first domain implementation.
5. A2A: publish cards only for actual deployed agent services.
6. Continuous checks: nightly link/metadata validation and CI gates for every public repository.

## 9. Security and privacy

Public discovery metadata is untrusted input. It does not authenticate a publisher, establish ownership, authorize an action, or grant access. The ecosystem's private operations repository must never be listed in public indexes beyond a non-sensitive aggregate count. Never copy private operational details into prompts, docs, MCP resources, or A2A cards.
