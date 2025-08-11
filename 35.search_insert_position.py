class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while(l < r):
            m = l+(r-l)//2
            n = nums[m]
            if target == n:
                return m
            elif target > n:
                l = m + 1
            else:
                r = m - 1
        if target > nums[l]:
            return l+1
        return l
