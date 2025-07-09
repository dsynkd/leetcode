class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        output = set()

        def dfs(i, combo):
            if i == len(nums):
                output.add(tuple(sorted(combo)))
                return
            dfs(i+1, combo)
            dfs(i+1, combo + [nums[i]])
        
        dfs(0, [])
        return [list(a) for a in output]