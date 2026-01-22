class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefixSum = nums.copy()
        for i in range(1, len(nums)):
            prefixSum[i] += prefixSum[i-1]
        return max(1, 1 - min(prefixSum))