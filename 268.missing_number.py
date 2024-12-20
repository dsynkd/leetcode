# Time Complexity: O(n.log(n)), sort
# Verdict: Pass

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                return nums[i-1]+1
        return nums[-1]+1