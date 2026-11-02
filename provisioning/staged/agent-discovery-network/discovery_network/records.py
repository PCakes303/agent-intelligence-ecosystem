"""Versioned discovery record and strict local validation."""

from __future__ import annotations

from dataclasses import dataclass
import math
from urllib.parse import urlparse


class RecordValidationError(ValueError):
    """Raised when a discovery record is structurally invalid."""


MAX_RECORD_ID_CHARS = 128
MAX_KIND_CHARS = 32
MAX_SUBJECT_ID_CHARS = 256
MAX_ENDPOINT_CHARS = 2_048
MAX_ISSUER_ID_CHARS = 256
MAX_CAPABILITIES = 128
MAX_CAPABILITY_CHARS = 128
MAX_PROVENANCE_CHARS = 512
MAX_SIGNATURE_CHARS = 8_192


def _finite_float(value: object) -> float | None:
    """Convert numeric input safely, rejecting booleans, overflow and non-finite values."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    try:
        converted = float(value)
    except (OverflowError, ValueError):
        return None
    return converted if math.isfinite(converted) else None


@dataclass(frozen=True)
class DiscoveryRecord:
    record_id: str
    kind: str
    subject_id: str
    endpoint: str
    issuer_id: str
    issued_at: float
    expires_at: float
    capabilities: tuple[str, ...] = ()
    provenance: str = ""
    signature: str = ""

    def validate(self, *, now: float, max_lifetime_seconds: float) -> None:
        limits = (
            ("record_id", self.record_id, MAX_RECORD_ID_CHARS),
            ("kind", self.kind, MAX_KIND_CHARS),
            ("subject_id", self.subject_id, MAX_SUBJECT_ID_CHARS),
            ("endpoint", self.endpoint, MAX_ENDPOINT_CHARS),
            ("issuer_id", self.issuer_id, MAX_ISSUER_ID_CHARS),
            ("provenance", self.provenance, MAX_PROVENANCE_CHARS),
            ("signature", self.signature, MAX_SIGNATURE_CHARS),
        )
        for name, value, maximum in limits:
            if not isinstance(value, str) or not value.strip():
                raise RecordValidationError(f"{name} must be a non-empty string")
            if len(value) > maximum:
                raise RecordValidationError(f"{name} exceeds maximum length")

        if self.kind not in {"agent", "resource", "service"}:
            raise RecordValidationError("kind must be agent, resource or service")

        try:
            parsed = urlparse(self.endpoint)
            hostname = parsed.hostname
            # Accessing .port also validates malformed/out-of-range port syntax.
            parsed.port
        except ValueError as exc:
            raise RecordValidationError("endpoint is a malformed URL") from exc
        if (
            parsed.scheme != "https"
            or not parsed.netloc
            or not hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.fragment
            or any(ch.isspace() for ch in self.endpoint)
        ):
            raise RecordValidationError("endpoint must be a valid HTTPS URL without credentials or fragment")

        now_value = _finite_float(now)
        if now_value is None:
            raise RecordValidationError("now must be a finite timestamp")
        max_lifetime_value = _finite_float(max_lifetime_seconds)
        if max_lifetime_value is None or max_lifetime_value <= 0:
            raise RecordValidationError("max_lifetime_seconds must be a finite positive number")

        issued_value = _finite_float(self.issued_at)
        if issued_value is None:
            raise RecordValidationError("issued_at must be a finite timestamp")
        expires_value = _finite_float(self.expires_at)
        if expires_value is None:
            raise RecordValidationError("expires_at must be a finite timestamp")
        if issued_value > now_value:
            raise RecordValidationError("issued_at cannot be in the future")
        if expires_value <= issued_value:
            raise RecordValidationError("expires_at must be later than issued_at")
        if expires_value <= now_value:
            raise RecordValidationError("record is expired")
        if expires_value - issued_value > max_lifetime_value:
            raise RecordValidationError("record lifetime exceeds configured maximum")

        if not isinstance(self.capabilities, tuple) or len(self.capabilities) > MAX_CAPABILITIES:
            raise RecordValidationError("capabilities must be a bounded tuple of strings")
        for capability in self.capabilities:
            if not isinstance(capability, str) or not capability.strip():
                raise RecordValidationError("capabilities must contain non-empty strings")
            if len(capability) > MAX_CAPABILITY_CHARS:
                raise RecordValidationError("capability identifier exceeds maximum length")
