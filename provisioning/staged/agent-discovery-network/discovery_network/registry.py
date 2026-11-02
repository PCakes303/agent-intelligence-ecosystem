"""Single-process discovery index with fail-closed trust filters."""

from __future__ import annotations

from collections.abc import Callable
import math
import threading
import time

from .records import DiscoveryRecord, RecordValidationError, _finite_float

Verifier = Callable[[DiscoveryRecord], bool]
TrustEvaluator = Callable[[str], bool]


class DiscoveryRegistry:
    """Prototype index; callbacks must be backed by real trust services in production."""

    def __init__(
        self,
        *,
        verifier: Verifier | None,
        trust_evaluator: TrustEvaluator | None,
        clock: Callable[[], float] = time.time,
        max_lifetime_seconds: float = 86_400.0,
        max_records: int = 10_000,
    ) -> None:
        lifetime_value = _finite_float(max_lifetime_seconds)
        if lifetime_value is None or lifetime_value <= 0:
            raise ValueError("max_lifetime_seconds must be a finite positive number")
        if isinstance(max_records, bool) or not isinstance(max_records, int) or max_records <= 0:
            raise ValueError("max_records must be a positive integer")
        self.verifier = verifier
        self.trust_evaluator = trust_evaluator
        self.clock = clock
        self.max_lifetime_seconds = lifetime_value
        self.max_records = max_records
        self._records: dict[str, DiscoveryRecord] = {}
        self._lock = threading.RLock()

    def _now(self) -> float:
        try:
            now = self.clock()
        except Exception as exc:
            raise RuntimeError("discovery clock unavailable") from exc
        now_value = _finite_float(now)
        if now_value is None:
            raise RuntimeError("discovery clock returned an invalid timestamp")
        return now_value

    def publish(self, record: DiscoveryRecord) -> None:
        now = self._now()
        record.validate(now=now, max_lifetime_seconds=self.max_lifetime_seconds)
        if self.verifier is None or self.trust_evaluator is None:
            raise PermissionError("verification and trust evaluators are required")
        try:
            if self.verifier(record) is not True:
                raise PermissionError("record signature verification denied")
            if self.trust_evaluator(record.issuer_id) is not True:
                raise PermissionError("record issuer is not trusted")
        except PermissionError:
            raise
        except Exception as exc:
            raise PermissionError("verification or trust evaluation failed") from exc

        with self._lock:
            self._prune_locked(now)
            if record.record_id in self._records:
                raise ValueError("record_id already exists")
            if len(self._records) >= self.max_records:
                raise OverflowError("discovery registry capacity reached")
            self._records[record.record_id] = record

    def query(
        self,
        *,
        kind: str | None = None,
        capability: str | None = None,
        issuer_id: str | None = None,
    ) -> list[DiscoveryRecord]:
        now = self._now()
        with self._lock:
            self._prune_locked(now)
            candidates = [
                record for record in self._records.values()
                if (kind is None or record.kind == kind)
                and (capability is None or capability in record.capabilities)
                and (issuer_id is None or record.issuer_id == issuer_id)
            ]

        # Re-evaluate trust at read time so revoked/untrusted issuers disappear.
        if self.verifier is None or self.trust_evaluator is None:
            return []
        accepted = []
        for record in candidates:
            try:
                if (
                    record.expires_at > now
                    and self.verifier(record) is True
                    and self.trust_evaluator(record.issuer_id) is True
                ):
                    accepted.append(record)
            except Exception:
                continue
        return accepted

    def _prune_locked(self, now: float) -> None:
        expired = [key for key, record in self._records.items() if record.expires_at <= now]
        for key in expired:
            del self._records[key]

    def __len__(self) -> int:
        now = self._now()
        with self._lock:
            self._prune_locked(now)
            return len(self._records)
