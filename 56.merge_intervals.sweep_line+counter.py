from collections import defaultdict

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        events = defaultdict(int)
        
        for start,end in intervals:
            events[start] += 1
            events[end] -= 1
        
        positions = sorted(events.keys())

        res = []
        active_count = 0
        cur_start = 0

        for pos in positions:
            if not active_count and events[pos] >= 0: # start new interval
                cur_start = pos
            active_count += events[pos]
            if not active_count:
                res.append([cur_start, pos])
        
        return res
