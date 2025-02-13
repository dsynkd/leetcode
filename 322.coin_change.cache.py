class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        cache = dict()

        def dfs(target) -> int:
            if target == 0:
                return 0
            if target in cache:
                return cache[target]
            res = -1
            for c in coins:
                if c > target:
                    continue
                m = 1 + dfs(target - c)
                if m > 0 and (res == -1 or m < res):
                    res = m
            cache[target] = res
            return res
        
        return dfs(amount)