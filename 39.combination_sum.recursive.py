# Approach: Recursive, similar to backtracking solution but we use index `j` now to
# keep track of where we are in the `nums` array instead of popping and appending
# This is to show that all (?) backtracking solutions can be implemented recursively by just passing
# in a single additional parameter to the recursive call
# Verdict: Pass

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        output = []

        def dfs(combo, j, target):
            if target == 0:
                output.append(combo)
                return
            if target < 0 or j >= len(nums):
                return
            
            dfs(combo + [nums[j]], j, target - nums[j])
            dfs(combo, j+1, target)
        
        dfs([], 0, target)
        return output