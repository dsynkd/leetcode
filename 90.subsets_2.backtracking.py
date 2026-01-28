class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(i: int):
            if i == len(nums):
                res.append(path.copy())
                return
            n = nums[i]
            path.append(n)
            dfs(i+1)
            path.pop()
            while i < len(nums) and nums[i] == n:
                i += 1
            dfs(i)
        
        dfs(0)
        return res