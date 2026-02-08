class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if s[i] == '0':
                if not '1' <= s[i-1] <= '2':
                    return 0
                dp[i] = dp[i-2] if i >= 2 else dp[i-1]
            else:
                dp[i] = dp[i-1]
                if s[i-1] == '1' or (s[i-1] == '2' and '0' <= s[i] <= '6'):
                    dp[i] += dp[i-2] if i >= 2 else 1

        return dp[-1]