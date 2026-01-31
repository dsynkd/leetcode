class Solution:
    def maxSubArrayLen(self, nums: list[int], k: int) -> int:
        res = 0
        indices = dict()
        indices[0] = -1
        prefixSum = 0
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            if (prefixSum - k) in indices:
                res = max(res, i - indices[prefixSum - k])
            if prefixSum not in indices:
                indices[prefixSum] = i
        
        return res