class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def dfs(head, tail):
            res.append(head)
            for i in range(len(tail)):     
                if i > 0 and tail[i] == tail[i-1]:
                    continue
                dfs(head + [tail[i]], tail[i+1:])
        
        dfs([], nums)
        return res