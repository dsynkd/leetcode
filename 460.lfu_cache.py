from collections import OrderedDict, defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counter = dict()
        self.freq = defaultdict(OrderedDict)
        self.min_freq = 0

    def _insert(self, key, value=None) -> int:
        count = self.counter[key]
        oldVal = self.freq[count].pop(key)
        if not value:
            value = oldVal
        if not self.freq[count] and count == self.min_freq:
            self.min_freq += 1
        self.freq[count + 1][key] = value
        self.counter[key] += 1
        return value

    def get(self, key: int) -> int:
        if key not in self.counter:
            return -1
        return self._insert(key)

    def put(self, key: int, value: int) -> None:
        if key in self.counter:
            self._insert(key, value)
            return
        
        if len(self.counter) == self.capacity:
            lfu = self.freq[self.min_freq].popitem(False)
            self.counter.pop(lfu[0])
    
        self.counter[key] = 0
        self.freq[0][key] = value
        self.min_freq = 0