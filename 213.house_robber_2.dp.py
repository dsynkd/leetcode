# Approach: Dynamic Programming
# Time Complexity: O(n) where n = len(nums)
# Verdict: Pass

class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        # Maintain two DP arrays:
        # 1. When we rob the first house and not the last
        # 2. When we rob the last house and not the first
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, n):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
        return max(dp1[-2], dp2[-1])
                