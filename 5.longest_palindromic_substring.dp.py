class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        dp = [[False for _ in range(L)] for _ in range(L)]
        res = ''

        for l in range(L):
            for j in range(l, L):
                i = j - l
                if s[i] == s[j] and (l <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if l+1 > len(res):
                        res = s[i:j+1]
        return res