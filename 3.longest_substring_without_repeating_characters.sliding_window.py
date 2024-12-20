# Approach: Sliding Window
# Verdict: Pass

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i,j = 0,1
        maxL = 1
        map = dict()
        map[s[0]] = 0

        while j < len(s):
            jc = s[j]
            if jc in map:
                index = map[jc]
                for c in [s[i] for i in range(i, index+1)]:
                    del map[c]
                i = index+1
            else:
                if j-i+1 > maxL:
                    maxL = j-i+1
            map[jc] = j
            j += 1

        return maxL