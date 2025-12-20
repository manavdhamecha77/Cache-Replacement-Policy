class Cache:
    """
    Fixed-size cache implementation.

    The Cache is responsible for:
    - Managing stored items
    - Detecting hits and misses
    - Delegating eviction decisions to an eviction policy

    The cache itself does NOT decide which item to evict.
    """

    def __init__(self, capacity, policy):
        """
        Initialize the cache.

        Args:
            capacity (int): Maximum number of items the cache can hold.
            policy (CachePolicy): Eviction policy instance (e.g., LRU, FIFO).
        """
        self.capacity = capacity
        self.container = []
        self.policy = policy

    def access(self, item):
        """
        Access an item in the cache.

        Args:
            item: The item being accessed.

        Returns:
            str: "Hit" if item exists in cache,
                 otherwise "Miss, evicted <item>".
        """
        # Cache HIT
        if item in self.container:
            self.policy.update_recency(self.container, item)
            return "Hit"

        # Cache MISS
        victim = None
        if len(self.container) == self.capacity:
            victim = self._evict()

        self.container.append(item)
        return f"Miss, evicted {victim}"

    def _evict(self):
        """
        Evict one item from the cache using the eviction policy.

        Returns:
            The evicted item.
        """
        victim = self.policy.find_victim(self.container)
        self.container.remove(victim)
        return victim
