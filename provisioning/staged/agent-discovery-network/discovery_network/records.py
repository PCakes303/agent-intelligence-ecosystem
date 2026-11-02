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

        if isinstance(now, bool) or not isinstance(now, (int, float)) or not math.isfinite(now):
            raise RecordValidationError("now must be a finite timestamp")
        if (
            isinstance(max_lifetime_seconds, bool)
            or not isinstance(max_lifetime_seconds, (int, float))
            or not math.isfinite(max_lifetime_seconds)
            or max_lifetime_seconds <= 0
        ):
            raise RecordValidationError("max_lifetime_seconds must be a finite positive number")

        for name, value in (("issued_at", self.issued_at), ("expires_at", self.expires_at)):
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise RecordValidationError(f"{name} must be a finite timestamp")
        if self.issued_at > now:
            raise RecordValidationError("issued_at cannot be in the future")
        if self.expires_at <= self.issued_at:
            raise RecordValidationError("expires_at must be later than issued_at")
        if self.expires_at <= now:
            raise RecordValidationError("record is expired")
        if self.expires_at - self.issued_at > max_lifetime_seconds:
            raise RecordValidationError("record lifetime exceeds configured maximum")

        if not isinstance(self.capabilities, tuple) or len(self.capabilities) > MAX_CAPABILITIES:
            raise RecordValidationError("capabilities must be a bounded tuple of strings")
        for capability in self.capabilities:
            if not isinstance(capability, str) or not capability.strip():
                raise RecordValidationError("capabilities must contain non-empty strings")
            if len(capability) > MAX_CAPABILITY_CHARS:
                raise RecordValidationError("capability identifier exceeds maximum length")
