from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0] += 1
        res = 0
        Z = 0
        for n in nums:
            Z += n
            res += counter[Z - k]
            counter[Z] += 1
        return res