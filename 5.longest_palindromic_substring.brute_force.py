class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                p = s[i:j]
                if p[::-1] == p and len(p) > len(res):
                    res = p
        return res