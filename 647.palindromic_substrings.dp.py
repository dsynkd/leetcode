# Approach: Same as "5. Longest Palindromic Susbtring"
## Same DP approach, but at each True site, we increment a counter instead of updating the longest palindrome
# Time Complexity: O(n^2)
# Verdict: Pass

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        count = 0
        for l in range(n):
            for i in range(n-l):
                j = i + l
                if s[i] == s[j]:
                    # if l is 0 or 1, we do not need to check dp
                    if l < 2 or dp[i+1][j-1]:
                        dp[i][j] = True
                        count += 1
        return count