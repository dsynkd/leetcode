class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 3:
            return max(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]