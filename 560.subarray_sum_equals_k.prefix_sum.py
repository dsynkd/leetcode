from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0] += 1
        res = 0
        sum = 0
        for n in nums:
            sum += n
            res += counter[sum - k]
            counter[sum] += 1
        return res