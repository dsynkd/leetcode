class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(i: int):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            while i < len(nums)-1 and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res