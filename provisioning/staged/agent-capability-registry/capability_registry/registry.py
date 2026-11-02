import threading


class CapabilityRegistry:
    def __init__(self, decision_callback=None, max_entries=10000):
        if max_entries < 1:
            raise ValueError('max_entries must be positive')
        self.decision_callback = decision_callback
        self.max_entries = max_entries
        self._items = {}
        self._lock = threading.RLock()

    def register(self, item):
        item.validate()
        key = (item.agent_id, item.capability_id)
        with self._lock:
            if key in self._items:
                raise ValueError('duplicate declaration')
            if len(self._items) >= self.max_entries:
                raise OverflowError('capacity reached')
            self._items[key] = item

    def match(self, requirements):
        requested = list(requirements)
        if not requested:
            raise ValueError('requirements cannot be empty')
        for req in requested:
            req.validate()
        with self._lock:
            candidates = list(self._items.values())
        found = []
        for item in candidates:
            if not all(item.capability_id == req.capability_id and all(item.attributes.get(k) == v for k, v in req.attributes.items()) for req in requested):
                continue
            if self.decision_callback is None:
                continue
            try:
                if self.decision_callback(item.agent_id, item) is True:
                    found.append(item)
            except Exception:
                continue
        return sorted(found, key=lambda item: (item.agent_id, item.capability_id))

    def __len__(self):
        with self._lock:
            return len(self._items)
