# Time Complexity: O(n.log(n)), sort
# Verdict: Pass

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return nums[-1]+1