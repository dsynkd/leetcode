class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        prefix = suffix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[-i-1] * (suffix or 1)
            res = max(res, prefix, suffix)
        return res