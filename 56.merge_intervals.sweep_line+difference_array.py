from collections import defaultdict

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        diff = defaultdict(int)
        for i,j in intervals:
            diff[i] += 1
            diff[j] -= 1
        
        s,c,res = 0,0,[]
        for p in sorted(diff.keys()):
            if c == 0 and diff[p] >= 0:
                s = p
            c += diff[p]
            if c == 0:
                res.append([s, p])
        return res