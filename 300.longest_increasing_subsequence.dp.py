# Approach: Dynamic Programming
# Time Complexity: O(n^2)
# Verdict: Pass

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        N = len(nums)
        dp = [1] * N
        for i in range(N-2, -1, -1):
            for j in range(i+1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)