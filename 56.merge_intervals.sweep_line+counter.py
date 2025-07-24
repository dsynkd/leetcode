from collections import defaultdict

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        counter = defaultdict(int)
        for i,j in intervals:
            counter[i] += 1
            counter[j] -= 1
        
        pos = sorted(counter.keys())
        c = 0 # counter
        s = 0 # current start
        res = []
        for k in pos:
            if c == 0 and counter[k] >= 0:
                s = k
            c += counter[k]
            if c == 0:
                res.append([s, k])
        return res