class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        n = newInterval
        for i,a in enumerate(intervals):
            if a[1] < n[0]:
                res.append(a)
            elif a[0] <= n[1]:
                n = [min(a[0], n[0]), max(a[1], n[1])]
            else:
                return res + [n] + intervals[i:]
        return res + [n]