import heapq
from typing import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        topK = heapq.nlargest(len(count), count, key=count.get)
        output = ''
        for c in topK:
            output += count[c] * c
        return output