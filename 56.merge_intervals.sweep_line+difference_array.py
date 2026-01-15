from collections import defaultdict

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        diff = defaultdict(int)
        for i,j in intervals:
            diff[i] += 1
            diff[j] -= 1
        
        c = 0
        s = 0
        res = []
        for k in sorted(diff.keys()):
            if c == 0 and diff[k] >= 0:
                s = k
            c += diff[k]
            if c == 0:
                res.append([s, k])
        return res