class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == '0':
            return 0

        dp = [1] + [0] * (n-1)

        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] > '2' or s[i-1] == '0':
                    return 0
                if i < 2:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-2]
            elif 10 <= int(s[i-1] + s[i]) <= 26:
                if i < 2:
                    dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:                
                dp[i] = dp[i-1]

        return dp[-1]