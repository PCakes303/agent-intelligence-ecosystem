"""Bounded local capability index and fail-closed candidate matching."""
import threading

from .models import Capability, Requirement


class CapabilityRegistry:
    """Single-process prototype; policy callback must use a trusted policy service."""

    def __init__(self, decision_callback=None, max_entries=10000):
        if not isinstance(max_entries, int) or isinstance(max_entries, bool) or max_entries < 1:
            raise ValueError("max_entries must be a positive integer")
        self.decision_callback = decision_callback
        self.max_entries = max_entries
        self._items = {}
        self._lock = threading.RLock()

    def register(self, item: Capability):
        item.validate()
        key = (item.agent_id, item.capability_id)
        with self._lock:
            if key in self._items:
                raise ValueError("duplicate declaration")
            if len(self._items) >= self.max_entries:
                raise OverflowError("capacity reached")
            self._items[key] = item

    def match(self, requirements):
        requested = list(requirements)
        if not requested:
            raise ValueError("requirements cannot be empty")
        for req in requested:
            req.validate()
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
