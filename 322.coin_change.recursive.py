# Approach: Recursive
# Time Complexity: O(n^t) where n = amount, t=len(coins)
# Verdict: TLE

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        def dfs(target) -> int|float:
            if target == 0:
                return 0
            res = float('inf')
            for c in coins:
                if c > target:
                    continue
                res = min(res, 1 + dfs(target - c))
            return res
        
        res = dfs(amount)
        return -1 if res == float('inf') else int(res)