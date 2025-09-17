class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 4:
            return max(nums)
        # Include first house, not last house
        dp1 = [nums[0], max(nums[0], nums[1])]
        # Include last house (i+1 later in code covers it), not first house
        dp2 = [nums[1], max(nums[1], nums[2])]
        
        for i in range(2, len(nums)-1):
            dp1.append(max(dp1[i-2] + nums[i], dp1[i-1]))
            dp2.append(max(dp2[i-2] + nums[i+1], dp2[i-1]))

        return max(dp1[-1], dp2[-1])