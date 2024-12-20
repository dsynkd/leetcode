# Approach: Dynamic Programming + Sliding Window
# LPS(0,n): LPS(1,n-1)+2 if S[0] == S[n] else max(LPS(0,n-1), LPS(1,n))
# Decision version: LPS(0,N) = True if S[0] == S[n] and LPS(1,N-1) ("inner string")
# Time Complexity: O(n^2)
# Verdict: Pass

class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        dp = [[False for _ in range(L)] for _ in range(L)]
        res = ""

        # Sliding Window where `l+1` is the length of the window
        # Build upper triangle
        for l in range(L):
            for j in range(l, L):
                i = j - l
                if s[i] == s[j] and (l <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if l+1 > len(res):
                        res = s[i:j+1]
        return res