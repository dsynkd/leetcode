import random

class Solution:

    def __init__(self, w: list[int]):
        self.prefixSum = w
        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] += self.prefixSum[i - 1]

    def pickIndex(self) -> int:
        rand = random.randrange(self.prefixSum[-1])
        for i in range(len(self.prefixSum)):
            if rand < self.prefixSum[i]:
                return i
        assert(False)