class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        
        prefixSum = [0] + nums.copy()
        for i in range(1, n):
            prefixSum[i + 1] += prefixSum[i]
        
        suffixSum = nums.copy() + [0]
        for i in range(n, 1, -1):
            suffixSum[i - 1] += suffixSum[i]

        for i in range(n):
            if prefixSum[i] == suffixSum[i+1]:
                return i
        
        return -1