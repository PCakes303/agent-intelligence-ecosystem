# Schema registry

## Purpose
This repository catalogs versioned machine-readable contracts. JSON Schema Draft 2020-12 is the default dialect unless a schema declares otherwise.

## Rules
- Give each published schema a stable identifier and explicit version.
- Prefer additive optional fields for compatible evolution.
- Reject unknown critical discriminators; document extension points explicitly.
- Provide positive and negative examples and automated validation.
- Never treat schema validity as proof that content is truthful, safe, authorized, or semantically correct.

## Layout
Schemas are grouped by domain under `schemas/`. Each schema should have a corresponding example and tests before being marked stable.
