class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        sum = 0
        maxSum = -10000
        for n in nums:
            sum += n
            if n > sum:
                sum = n
            if sum > maxSum:
                maxSum = sum
        return maxSum