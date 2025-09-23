class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i,j = 0,0
        s = 0 # Current Sum
        res = len(nums)+1
        
        while j < len(nums):
            s += nums[j]
            while s >= target:
                res = min(res, j-i+1)
                s -= nums[i]
                i += 1
            j += 1
        
        return res if res != len(nums)+1 else 0