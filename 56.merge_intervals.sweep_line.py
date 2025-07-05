from collections import defaultdict

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        events = list()
        
        # (position, event_type, interval_id)
        # 0 event_type = start event, 1 event_type = end event
        for index,(start,end) in enumerate(intervals):
            events.append((start, 0, index))
            events.append((end, 1, index))
        
        # sort by position first, event type second
        # it's important to process a 'start event' before an 'end event' in the edge case that one position contains both events
        events.sort()

        res = []
        active = set()
        cur_start = 0

        for pos,event_type,index in events:
            if event_type == 0: # start event
                if not active:
                    cur_start = pos
                active.add(index)
            else: # end event
                active.remove(index)
                if not active:
                    res.append([cur_start, pos])
        
        return res
