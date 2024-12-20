# Similar to: "30. Substring with Concatenation of All Words"

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqMap = defaultdict(int)
        for s in s1:
            freqMap[s] += 1
        
        permL = len(s1)
        for i in range(len(s2)-permL+1):
            map = defaultdict(int)
            j = i
            while j < i + permL:
                c = s2[j]
                if map[c] < freqMap[c]:
                    map[c] += 1
                else:
                    break
                j += 1
            if j == i + permL:
                return True
                
        return False