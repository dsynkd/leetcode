class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = len(nums)-1
        while i <= j:
            m = i + (j-i)//2
            if nums[m] == target:
                a,b = m,m
                while a >= 0 and nums[a] == target:
                    a -= 1
                while b < len(nums) and nums[b] == target:
                    b += 1
                return [a+1, b-1]
            elif nums[m] > target:
                j = m-1
            else:
                i = m+1
        return [-1,-1]