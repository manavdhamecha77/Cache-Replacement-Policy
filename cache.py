class Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.container = []   # cache storage (MRU at index 0)

    def access(self, item):
        # Case 1: Cache HIT
        if item in self.container:
            # Update recency
            self.container.remove(item)
            self.container.insert(0, item)
            return "Hit"

        # Case 2: Cache MISS
        if len(self.container) >= self.capacity:
            victim = self.evict()
            self.container.insert(0, item)
            return f"Miss, evicted {victim}"

        # Case 3: Miss but space available
        self.container.insert(0, item)
        return "Miss, added without eviction"

    def evict(self):
        # LRU eviction = remove last element
        return self.container.pop()

