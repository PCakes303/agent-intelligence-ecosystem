"""Local AIX envelope fixture validation; no messages are transmitted."""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

class FixtureError(ValueError):
    """Raised when a protocol fixture is malformed."""

_SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "agent-envelope.schema.json"
_SCHEMA = json.loads(_SCHEMA_PATH.read_text(encoding="utf-8"))
_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())

def _time(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise FixtureError("timestamps must include a timezone")
    return parsed

def validate_envelope(envelope: Mapping[str, Any]) -> dict[str, Any]:
    errors = sorted(_VALIDATOR.iter_errors(envelope), key=lambda e:(list(e.absolute_path),e.message))
    if errors:
        first=errors[0]
        location=".".join(str(part) for part in first.absolute_path) or "<root>"
        raise FixtureError(f"envelope schema error at {location}: {first.message}")
    created=_time(envelope["created_at"])
    expires=_time(envelope["expires_at"])
    if expires <= created or (expires-created).total_seconds() > envelope["ttl_seconds"]:
        raise FixtureError("envelope expiry must be after creation and within TTL")
    return {"status":"PASS","message_id":envelope["message_id"],"scope":"synthetic local fixture only"}
