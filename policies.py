class Cache_policy:
    def find_victim(self, container):
        raise NotImplementedError
        
    def update_recency(self, container, item):
        raise NotImplementedError


class LRU_policy(Cache_policy):
    def find_victim(self, container):
        return container[0]

    def update_recency(self, container, item):
        container.remove(item)
        container.append(item)


class FIFO_policy(Cache_policy):
    def find_victim(self, container):
        return container[0]

    def update_recency(self, container, item):
        pass
