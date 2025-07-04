class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        b = newInterval
        res = []
        for i in range(len(intervals)):
            a = intervals[i]
            if b[0] > a[1]:
                res.append(a)
            elif b[1] < a[0]:
                res.append(b)
                return res + intervals[i:]
            else:
                b = [min(a[0], b[0]), max(a[1], b[1])]
        res.append(b)
        return res