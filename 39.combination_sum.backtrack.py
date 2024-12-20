# Approach: Backtracking
# Verdict: Pass

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        output = []

        def dfs(combo, target):
            if target == 0:
                output.append(combo)
                return
            if target < 0 or not nums:
                return
            
            num = nums.pop()
            dfs(combo, target)

            # Backtrack
            nums.append(num)
            dfs(combo + [num], target - num)

        dfs([], target)
        return output