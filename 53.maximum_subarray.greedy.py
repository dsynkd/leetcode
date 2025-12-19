class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        s = 0
        res = -10000
        for n in nums:
            s += n
            if n > s:
                s = n
            res = max(res, s)
        return res