from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events = defaultdict(int)
        for start,end in intervals:
            events[start] += 1
            events[end] -= 1
        
        pos = sorted(events.keys())
        r = 0
        c = 0
        for p in pos:
            r = max(r, c := c + events[p])
        
        return r