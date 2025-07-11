class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]
            if cur[0] <= last[1]: #overlap
                last[1] = max(cur[1], last[1])
            else:
                res.append(cur)

        return res