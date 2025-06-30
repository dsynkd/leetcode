from collections import Counter

class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        self.counter = Counter(nums)
        p = []

        def dfs(i: int):
            if i == len(nums):
                res.append(p.copy())
                return
            for c in self.counter:
                if not self.counter[c]:
                    continue
                p.append(c)
                self.counter[c] -= 1
                dfs(i + 1)
                p.pop()
                self.counter[c] += 1
        
        dfs(0)
        return res