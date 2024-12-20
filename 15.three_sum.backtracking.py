# Subset of combination sum with k == 3 and target == 0, so using same backtracking approach as combination sum here
# Verdict: MLE

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        k = 3

        def dfs(combo, target):
            if target == 0 and len(combo) == k:
                output.append(combo)
                return
            if target < 0 or not nums:
                return
            
            num = nums.pop()
            dfs(combo, target)
            nums.append(num)
            dfs(combo + [num], target - num) 
        
        dfs([], 0)
        return output