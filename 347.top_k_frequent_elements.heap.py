# Approach: Heap
# Time Complexity: O(n log(n))

from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count, key=count.get)