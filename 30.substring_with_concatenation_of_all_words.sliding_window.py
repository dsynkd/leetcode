from collections import Counter, defaultdict
from copy import deepcopy

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        L = len(words[0])
        permL = L * len(words)
        wordCount = Counter(words)
        res = []
        i = 0
        while i <= len(s) - permL:
            j = i
            counter = defaultdict(int)
            c = 0
            while j-i < permL and (word := s[j:j+L]) in wordCount:
                counter[word] += 1
                if counter[word] > wordCount[word]:
                    break
                j += L
            if j - i == permL:
                res.append(i)
            i += 1
        
        return res