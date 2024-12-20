# Greedy ("Kadane's Algorithm"): at any given point, if current number is bigger than the sum,
# then we can 'restart' the sum at current index
# Time Complexity: Linear O(N)
# Verdict: Pass

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