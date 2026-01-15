from collections import defaultdict

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        E = list()
        for x,(i,j) in enumerate(intervals):
            E.append((i, 0, x))
            E.append((j, 1, x))
        E.sort()

        res = []
        A = set()
        s = 0

        for p,e,x in E:
            # Start Event
            if e == 0:
                if not A:
                    s = p
                A.add(x)
            # End Event
            else:
                A.remove(x)
                if not A:
                    res.append([s, p])
        
        return res
