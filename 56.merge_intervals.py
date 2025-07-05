class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        i = 1
        res = [intervals[0]]
        while i < len(intervals):
            cur = intervals[i]
            last = res[-1]
            if cur[0] <= last[1]: #overlap
                last[1] = max(cur[1], last[1])
            else:
                res.append(cur)
            i += 1
        return res