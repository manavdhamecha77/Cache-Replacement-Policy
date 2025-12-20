class Cache:
    def __init__(self, capacity, policy):
        self.capacity = capacity
        self.container = []
        self.policy = policy

    def access(self, item):
        if item in self.container:
            self.policy.update_recency(self.container, item)
            return "Hit"

        victim = None
        if len(self.container) == self.capacity:
            victim = self._evict()

        self.container.append(item)
        return f"Miss, evicted {victim}"

    def _evict(self):
        victim = self.policy.find_victim(self.container)
        self.container.remove(victim)
        return victim
