class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(i: int, path: list[int]):
            if i == len(nums):
                res.append(path)
                return
            dfs(i+1, path + [nums[i]])
            dfs(i+1, path)
        
        dfs(0, [])
        return res