class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        prevEnd = intervals[0][1]
        res = 0

        for i,j in intervals[1:]:
            if prevEnd > i:
                res += 1
            else:
                prevEnd = j
        
        return res