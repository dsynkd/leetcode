class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = ''

        for offset in range(n):
            for i in range(n - offset):
                j = i + offset
                window_size = offset + 1
                if s[i] == s[j] and (window_size <= 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if window_size > len(res):
                        res = s[i:i+window_size]
        return res