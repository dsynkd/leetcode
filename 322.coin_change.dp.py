class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for v in range(1, amount + 1):
            for c in coins:
                if c > v:
                    continue
                dp[v] = min(dp[v], 1 + dp[v - c])

        if dp[amount] == amount + 1:
            return -1
        return dp[amount]