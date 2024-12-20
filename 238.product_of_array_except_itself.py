# Trick: Compute list of prefixes and suffixes, such that at any point `i` in nums,
# prefix[i] * suffix[i] would give you the product of all elements in the array except array[i]
# nums = [1,2,3,4]
# prefix = [1, 2, 6, 24]
# suffix = [24, 12, 4, 1]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        return [prefix[i] * suffix[i] for i in range(n)]