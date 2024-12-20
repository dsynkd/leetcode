# Approach: Dynamic Programming
# We keep track of the minimum number so we can reset the subsequence count
# At each number, we backtrack to the length of longest increasing subsequence
# By checking the DP array at each point where the correspondign number was smaller than current number

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        def dfs(i, j):
            if i == len(nums):
                return 0
            
            LIS = dfs(i + 1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include
            
            return LIS

        return dfs(0, -1)