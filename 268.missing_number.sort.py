class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return nums[-1]+1