class Solution:
    def makePalindrome(self, s: str) -> bool:
        c = 0
        for i in range(len(s)//2):
            j = -i-1
            if s[i] != s[j]:
                c += 1
        return c < 3