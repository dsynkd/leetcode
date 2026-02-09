from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        assert(k <= len(nums))
        count = Counter(nums)
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