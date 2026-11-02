"""Small default-deny policy decision point prototype.

This is a deterministic contract-test reference, not a production authorization
system. Production enforcement must authenticate principals, protect policy
distribution, and fail closed when this evaluator is unavailable.
"""
from __future__ import annotations

import fnmatch
from typing import Any


def _matches(patterns: list[str], value: str) -> bool:
    return any(fnmatch.fnmatchcase(value, pattern) for pattern in patterns)


def evaluate(policy: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    principal = request.get("principal_id")
    action = request.get("action")
    resource = request.get("resource")
    scopes = set(request.get("scopes", []))
    if not all(isinstance(x, str) and x for x in (principal, action, resource)):
        return {"effect": "deny", "decision_id": "invalid-request", "matched_rules": [], "reason": "missing or invalid principal, action, or resource"}
    if not isinstance(request.get("scopes", []), list):
        return {"effect": "deny", "decision_id": "invalid-request", "matched_rules": [], "reason": "scopes must be an array"}

    allows: list[str] = []
    denies: list[str] = []
    for rule in policy.get("rules", []):
        if not _matches(rule.get("principals", []), principal):
            continue
        if not _matches(rule.get("actions", []), action):
            continue
        if not _matches(rule.get("resources", []), resource):
            continue
        if not set(rule.get("required_scopes", [])).issubset(scopes):
            continue
        (allows if rule.get("effect") == "allow" else denies).append(rule.get("id", "unnamed-rule"))

    if denies:
        return {"effect": "deny", "decision_id": "explicit-deny", "matched_rules": sorted(denies), "reason": "an explicit deny rule matched"}
    if allows:
        return {"effect": "allow", "decision_id": "explicit-allow", "matched_rules": sorted(allows), "reason": "one or more allow rules matched and no deny rule matched"}
    return {"effect": "deny", "decision_id": "default-deny", "matched_rules": [], "reason": "no allow rule matched"}


def validate_and_evaluate(policy: dict[str, Any], request: dict[str, Any], policy_schema: dict[str, Any], request_schema: dict[str, Any]) -> dict[str, Any]:
    from jsonschema import Draft202012Validator
    pv = list(Draft202012Validator(policy_schema).iter_errors(policy))
    rv = list(Draft202012Validator(request_schema).iter_errors(request))
    if pv or rv:
        return {"effect": "deny", "decision_id": "invalid-input", "matched_rules": [], "reason": "policy or request failed schema validation",
                "validation_errors": [e.message for e in pv + rv]}
    return evaluate(policy, request)
