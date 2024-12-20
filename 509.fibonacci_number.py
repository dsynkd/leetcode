class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [1,1]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]