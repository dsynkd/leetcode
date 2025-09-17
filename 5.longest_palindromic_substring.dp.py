class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = ''

        for window_length in range(n):
            for i in range(n - window_length):
                j = i + window_length
                if s[i] == s[j] and (window_length <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if window_length+1 > len(res):
                        res = s[i:j+1]
        return res