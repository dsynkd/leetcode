class RandomizedSet:

    def __init__(self):
        self.cache = dict()
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.cache:
            return False
        self.cache[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache:
            return False
        index = self.cache[val]
        self.values[index], self.values[-1] = self.values[-1], self.values[index]
        self.cache[self.values[index]] = index
        self.values.pop()
        del self.cache[val]
        return True

    def getRandom(self) -> int:
        return self.values[randint(0, len(self.values)-1)]
