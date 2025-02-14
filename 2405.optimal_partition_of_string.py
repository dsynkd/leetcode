class Solution:
    def partitionString(self, s: str) -> int:
        substrings = []
        sub = ''
        for c in s:
            if c in sub:
                substrings.append(sub)
                sub = c
            else:
                sub += c
        res = len(substrings)
        if sub:
            res += 1
        return res