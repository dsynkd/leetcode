# HashMap: A simple use case

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagram = defaultdict(int)
        for c in s:
            anagram[c] += 1
        
        for c in t:
            if anagram[c] <= 0:
                return False
            anagram[c] -= 1

        return True