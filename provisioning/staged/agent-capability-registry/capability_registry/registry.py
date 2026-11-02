"""Bounded local capability index and fail-closed candidate matching."""
import threading
from types import MappingProxyType

from .models import Capability, Requirement


class CapabilityRegistry:
    """Single-process prototype; policy callback must use a trusted policy service."""

    def __init__(self, decision_callback=None, max_entries=10000, max_requirements=128):
        if not isinstance(max_entries, int) or isinstance(max_entries, bool) or max_entries < 1:
            raise ValueError("max_entries must be a positive integer")
        if not isinstance(max_requirements, int) or isinstance(max_requirements, bool) or max_requirements < 1:
            raise ValueError("max_requirements must be a positive integer")
        self.decision_callback = decision_callback
        self.max_entries = max_entries
        self.max_requirements = max_requirements
        self._items = {}
        self._lock = threading.RLock()

    def register(self, item: Capability):
        if not isinstance(item, Capability):
            raise TypeError("item must be a Capability")
        item.validate()
        # Snapshot and freeze caller-owned attributes so post-registration mutation
        # cannot change a validated declaration or what policy callbacks observe.
        stored = Capability(
            capability_id=item.capability_id,
            agent_id=item.agent_id,
            description=item.description,
            version=item.version,
            attributes=MappingProxyType(dict(item.attributes)),
        )
        stored.validate()
        key = (stored.agent_id, stored.capability_id)
        with self._lock:
            if key in self._items:
                raise ValueError("duplicate declaration")
            if len(self._items) >= self.max_entries:
                raise OverflowError("capacity reached")
            self._items[key] = stored

    def match(self, requirements):
        requested = []
        try:
            iterator = iter(requirements)
        except TypeError as exc:
            raise TypeError("requirements must be iterable") from exc
        for req in iterator:
            if len(requested) >= self.max_requirements:
                raise ValueError("too many requirements")
            if not isinstance(req, Requirement):
                raise TypeError("each requirement must be a Requirement")
            req.validate()
            # Snapshot requirement attributes to keep a stable matching input.
            requested.append(Requirement(
                capability_id=req.capability_id,
                attributes=MappingProxyType(dict(req.attributes)),
            ))
        if not requested:
            raise ValueError("requirements cannot be empty")

        with self._lock:
            candidates = list(self._items.values())

        by_agent = {}
        for item in candidates:
            by_agent.setdefault(item.agent_id, []).append(item)

        found = []
        for agent_id, declarations in by_agent.items():
            selected = []
            for req in requested:
                match = next((item for item in declarations
                              if item.capability_id == req.capability_id
                              and all(item.attributes.get(k) == v for k, v in req.attributes.items())), None)
                if match is None:
                    selected = []
                    break
                selected.append(match)
            if not selected or self.decision_callback is None:
                continue
            try:
                if all(self.decision_callback(agent_id, item) is True for item in selected):
                    found.extend(selected)
            except Exception:
                continue
        unique = {(item.agent_id, item.capability_id): item for item in found}
        return sorted(unique.values(), key=lambda item: (item.agent_id, item.capability_id))

    def __len__(self):
        with self._lock:
            return len(self._items)
