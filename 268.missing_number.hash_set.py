class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        numSet = set(nums)
        for i in range(len(nums)):
            if i not in numSet:
                return i
        return len(nums)