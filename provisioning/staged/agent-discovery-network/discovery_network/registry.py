"""Single-process discovery index with fail-closed trust filters."""

from __future__ import annotations

from collections.abc import Callable
import threading
import time

from .records import DiscoveryRecord, RecordValidationError

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
        if max_lifetime_seconds <= 0 or max_records <= 0:
            raise ValueError("limits must be positive")
        self.verifier = verifier
        self.trust_evaluator = trust_evaluator
        self.clock = clock
        self.max_lifetime_seconds = max_lifetime_seconds
        self.max_records = max_records
        self._records: dict[str, DiscoveryRecord] = {}
        self._lock = threading.RLock()

    def publish(self, record: DiscoveryRecord) -> None:
        now = self.clock()
        record.validate(now=now, max_lifetime_seconds=self.max_lifetime_seconds)
        if self.verifier is None or self.trust_evaluator is None:
            raise PermissionError("verification and trust evaluators are required")
        try:
            if not self.verifier(record):
                raise PermissionError("record signature verification denied")
            if not self.trust_evaluator(record.issuer_id):
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
        now = self.clock()
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
                if record.expires_at > now and self.verifier(record) and self.trust_evaluator(record.issuer_id):
                    accepted.append(record)
            except Exception:
                continue
        return accepted

    def _prune_locked(self, now: float) -> None:
        expired = [key for key, record in self._records.items() if record.expires_at <= now]
        for key in expired:
            del self._records[key]

    def __len__(self) -> int:
        with self._lock:
            self._prune_locked(self.clock())
            return len(self._records)
