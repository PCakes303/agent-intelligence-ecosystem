"""Strict validators for public compliance register metadata; not a legal decision engine."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator, FormatChecker

MAX_DOCUMENT_BYTES = 2_097_152
MAX_JSON_DEPTH = 32
SCHEMA_FILES = {
    "legal": "legal-register.schema.json",
    "controls": "control-catalog.schema.json",
    "evidence": "evidence-index.schema.json",
}

class RegistryError(ValueError):
    """Raised when a compliance metadata document is malformed or inconsistent."""

def _pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise RegistryError(f"duplicate JSON key: {key}")
        result[key] = value
    return result

def _reject_constant(value):
    raise RegistryError(f"non-standard JSON numeric constant: {value}")

def load_json(path: Path) -> Any:
    raw = path.read_bytes()
    if len(raw) > MAX_DOCUMENT_BYTES:
        raise RegistryError(f"{path.name} exceeds the byte limit")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RegistryError(f"{path.name} is not UTF-8") from exc
    depth = 0
    in_string = False
    escaped = False
    for char in text:
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
        elif char == '"':
            in_string = True
        elif char in "[{":
            depth += 1
            if depth > MAX_JSON_DEPTH:
                raise RegistryError(f"{path.name} exceeds the JSON nesting limit")
        elif char in "]}":
            depth -= 1
            if depth < 0:
                raise RegistryError(f"{path.name} has invalid JSON structure")
    try:
        return json.loads(text, object_pairs_hook=_pairs, parse_constant=_reject_constant)
    except RegistryError:
        raise
    except (json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise RegistryError(f"{path.name} contains invalid JSON") from exc

def _validate_schema(document: Any, schema_path: Path, label: str) -> None:
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(document), key=lambda e: (list(e.absolute_path), e.message))
    if errors:
        first = errors[0]
        location = ".".join(str(part) for part in first.absolute_path) or "<root>"
        raise RegistryError(f"{label} schema error at {location}: {first.message}")

def validate_documents(legal: dict, controls: dict, evidence: dict, schema_dir: Path) -> dict:
    _validate_schema(legal, schema_dir / SCHEMA_FILES["legal"], "legal register")
    _validate_schema(controls, schema_dir / SCHEMA_FILES["controls"], "control catalogue")
    _validate_schema(evidence, schema_dir / SCHEMA_FILES["evidence"], "evidence index")

    legal_ids = [item["id"] for item in legal["records"]]
    control_ids = [item["id"] for item in controls["controls"]]
    evidence_ids = [item["evidence_id"] for item in evidence["records"]]
    for label, values in (("legal record", legal_ids), ("control", control_ids), ("evidence record", evidence_ids)):
        if len(values) != len(set(values)):
            raise RegistryError(f"duplicate {label} id")

    legal_set = set(legal_ids)
    control_set = set(control_ids)
    for control in controls["controls"]:
        unknown = set(control["linked_legal_records"]) - legal_set
        if unknown:
            raise RegistryError(f"control {control['id']} references unknown legal records: {sorted(unknown)}")
    for record in evidence["records"]:
        unknown = set(record["control_ids"]) - control_set
        if unknown:
            raise RegistryError(f"evidence {record['evidence_id']} references unknown controls: {sorted(unknown)}")

    for record in legal["records"]:
        if date.fromisoformat(record["next_review"]) < date.fromisoformat(record["last_verified"]):
            raise RegistryError(f"legal record {record['id']} has next_review before last_verified")
    return {
        "legal_records": len(legal_ids),
        "controls": len(control_ids),
        "evidence_records": len(evidence_ids),
        "status": "valid",
        "legal_applicability_determined": False,
        "compliance_certification": False,
    }

def validate_repository(root: Path) -> dict:
    registry_dir = root / "registry"
    schema_dir = root / "schemas"
    return validate_documents(
        load_json(registry_dir / "legal-applicability.json"),
        load_json(registry_dir / "control-catalog.json"),
        load_json(registry_dir / "evidence-index.json"),
        schema_dir,
    )
