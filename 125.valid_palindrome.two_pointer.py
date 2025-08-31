class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isAlphaNumeric(c: str):
            return '0' <= c <= '9' or 'A' <= c <= 'Z' or 'a' <= c <= 'z'

        j = len(s)-1
        for i in range(len(s)):
            if not isAlphaNumeric(s[i]):
                continue
            while not isAlphaNumeric(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                j -= 1
        return True