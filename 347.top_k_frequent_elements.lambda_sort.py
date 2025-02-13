# HashMap + Sort: here we use a basic sorting algorithm using a lambda to get a sorted list of
# the keys of the hashmap based on their corresponding values, which represent frequency.
# Time Complexity: O(n.log(n)), main operation is the quick sort
# Verdict: Pass

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        vals = [k for k,v in sorted(Counter(nums).items(), key = lambda x: x[1])]
        return vals[-k:]