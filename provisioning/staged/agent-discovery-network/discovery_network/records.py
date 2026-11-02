"""Versioned discovery record and strict local validation."""

from __future__ import annotations

from dataclasses import dataclass
import math
from urllib.parse import urlparse


class RecordValidationError(ValueError):
    """Raised when a discovery record is structurally invalid."""


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
        for name in ("record_id", "kind", "subject_id", "endpoint", "issuer_id"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise RecordValidationError(f"{name} must be a non-empty string")
        if self.kind not in {"agent", "resource", "service"}:
            raise RecordValidationError("kind must be agent, resource or service")
        parsed = urlparse(self.endpoint)
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
            raise RecordValidationError("endpoint must be an HTTPS URL without embedded credentials")
        for name, value in (("issued_at", self.issued_at), ("expires_at", self.expires_at)):
            if not isinstance(value, (int, float)) or not math.isfinite(value):
                raise RecordValidationError(f"{name} must be a finite timestamp")
        if self.issued_at > now:
            raise RecordValidationError("issued_at cannot be in the future")
        if self.expires_at <= self.issued_at:
            raise RecordValidationError("expires_at must be later than issued_at")
        if self.expires_at <= now:
            raise RecordValidationError("record is expired")
        if self.expires_at - self.issued_at > max_lifetime_seconds:
            raise RecordValidationError("record lifetime exceeds configured maximum")
        if not isinstance(self.capabilities, tuple) or any(
            not isinstance(item, str) or not item.strip() for item in self.capabilities
        ):
            raise RecordValidationError("capabilities must be a tuple of non-empty strings")
        if not isinstance(self.provenance, str) or not self.provenance.strip():
            raise RecordValidationError("provenance must identify the publishing source")
        if not isinstance(self.signature, str) or not self.signature.strip():
            raise RecordValidationError("signature must be present for verifier evaluation")
