# Approach: Two Pointer
# Time Complexity: O(n^2), n for iterating through s, and n for iterating again during construction of l and r
# Verdict: Pass

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            l,r = i,i

            # Need to update left and right pointers to account for even length palindromes
            while l >= 0 and s[l] == s[i]:
                l -= 1
            while r < len(s) and s[r] == s[i]:
                r += 1

            # Now we count palindrome length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            palindrome = s[l+1:r]
            if len(palindrome) > len(res):
                res = palindrome

        return res