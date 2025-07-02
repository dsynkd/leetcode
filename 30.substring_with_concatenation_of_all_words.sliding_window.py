from collections import Counter, defaultdict
from copy import deepcopy

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        L = len(words[0]) # word length
        S = L * len(words) # substring size
        wordCount = Counter(words)
        res = []
        i = 0

        while i <= len(s) - S:
            j = i
            counter = defaultdict(int)
            c = 0
            while j-i < S and (word := s[j:j+L]) in wordCount and counter[word] < wordCount[word]:
                counter[word] += 1
                j += L
            if j - i == S:
                res.append(i)
            i += 1
        
        return res