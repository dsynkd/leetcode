# Bucket Sort: Distribute the numbers into buckets for each frequency. This will then allow us to iterate backwards from
# the length of the array, and each time we encounter a bucket, adding at most k elements from it to our output
# Time Complexity: O(n)

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        assert(k <= len(nums))
        count = Counter(nums)

        # cant use defaultdict here because it actually expands itself every time a value that does not exist in it
        # is accessed by adding a key-value pair mapped to the default value
        # This will "Memory Limit Exceed" in LeetCode
        freq = dict()
        for key,val in count.items():
            if val in freq:
                freq[val].append(key)
            else:
                freq[val] = [key]

        i = len(nums)
        output = []
        while k > 0:
            if i in freq:
                L = min(k, len(freq[i]))
                output += freq[i][0:L]
                k -= L
            i -= 1
        return output