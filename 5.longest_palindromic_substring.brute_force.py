# Approach: Two Pointer
# Time Complexity: O(n^3); n^2 for generating each substring and n for palindrome verification
# Verdict: Pass (!?)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        def isPalindrome(s: str) -> bool:
            # Any implementation from "125. Valid Palindrome"
            return s[::-1] == s

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                substring = s[i:j]
                if isPalindrome(substring) and len(substring) > len(res):
                    res = substring

        return res