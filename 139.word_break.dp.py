# Approach: Dynamic Programming
# Time Complexity: O(n^2)
# Verdict: Pass

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        S = len(s)
        dp = [False] * S
        for i in range(S-1, -1, -1):
            if s[i:] in wordSet:
                dp[i] = True
            else:
                for j in range(i, S):
                    if dp[j] and s[i:j] in wordSet:
                        dp[i] = True
        return dp[0]