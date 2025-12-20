class CachePolicy:
    """
    Abstract base class for cache eviction policies.

    Any eviction policy must implement:
    - find_victim(): decides which item to evict
    - update_recency(): updates policy state on access
    """

    def find_victim(self, container):
        """
        Select an item to evict from the cache.

        Args:
            container (list): Current cache contents.

        Returns:
            The item chosen for eviction.
        """
        raise NotImplementedError

    def update_recency(self, container, item):
        """
        Update internal policy state when an item is accessed.

        Args:
            container (list): Current cache contents.
            item: Accessed item.
        """
        raise NotImplementedError


class LRUPolicy(CachePolicy):
    """
    Least Recently Used (LRU) eviction policy.

    Evicts the item that has not been accessed for the longest time.
    """

    def find_victim(self, container):
        # Least recently used item is at the front
        return container[0]

    def update_recency(self, container, item):
        container.remove(item)
        container.append(item)


class FIFOPolicy(CachePolicy):
    """
    First-In First-Out (FIFO) eviction policy.

    Evicts the item that was inserted earliest.
    """

    def find_victim(self, container):
        return container[0]

    def update_recency(self, container, item):
        # FIFO does not update order on access
        pass
