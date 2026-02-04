class Solution:
    def coinChange(self, coins: list[int], amount: int):
        dp = [0] + [float('inf')] * amount

        for i in range(amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        return -1 if dp[amount] == float('inf') else dp[amount]
