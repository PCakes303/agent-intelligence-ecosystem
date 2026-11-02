# Capability contract v1

A declaration describes what an agent claims it can do. It is not proof that the capability works or that the agent is trusted.

Required fields: `capability_id`, `agent_id`, `description`, `version` (numeric major.minor.patch), and `attributes` (string key/value metadata). Unknown fields are rejected. Limits: 128 characters per identifier, 1,024 for description, 32 attributes, 256 characters per attribute value, and 10,000 indexed declarations by default.

A requirement matches an exact capability identifier and optional exact-match attributes. Every requested requirement must match. A candidate is returned only if the supplied policy callback returns true. Missing callbacks, false results and callback exceptions deny the candidate.

Results are sorted by agent identifier and capability identifier. Matching is advisory and does not reserve capacity or guarantee availability.
