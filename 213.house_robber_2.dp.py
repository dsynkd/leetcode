class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 4:
            return max(nums)
        dp1 = [0] * N
        dp2 = [0] * N
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[0], dp2[1] = 0, nums[1]
        for i in range(2, N):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
        return max(dp1[-2], dp2[-1])
                