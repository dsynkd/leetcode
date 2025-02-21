class Solution:
    def jump(self, nums: list[int]) -> int:
        i,j = 0,0
        jumps = 0

        while j < len(nums)-1:
            m = 0
            for a in range(i,j+1):
                m = max(m, a + nums[a])
            i = j+1
            j = m
            jumps += 1

        return jumps

print(Solution().jump([2,3,1,1,4]))