class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums)-1
        i = j-1
        while i >= 0:
            if nums[i] >= j-i:
                j = i
            i -= 1
        return j == 0