# Approach: Recursive (Brute Force)
# Time Complexity: O(2^n)
# Verdict: TLE

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        if s == "":
            return True
        wordSet = set(wordDict)
        L = len(s)
        for i in range(1, L+1):
            word = s[:i]
            if word in wordSet and self.wordBreak(s[i:], wordDict):
                return True
        return False