class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        events = []
        for i,x in enumerate(intervals):
            events.append([x[0], 1, i])
            events.append([x[1], 0, i])
        
        events.sort()

        r = 0
        c = 0
        for e in events:
            if e[1] == 1:
                c += 1
            else:
                c -= 1
            r = max(r, c)
        
        return r