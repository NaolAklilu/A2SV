class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        else:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.pop(key)
        if len(self.cache) == self.capacity:
            self.cache.pop(list(self.cache.keys())[0])
        self.cache[key] = value