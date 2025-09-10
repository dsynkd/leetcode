from collections import deque

class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[0][0] == timestamp:
            self.queue[0][1] += 1
        else:
            self.queue.append([timestamp, 1])
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0][0] <= timestamp-300:
            node = self.queue.popleft()
            self.total -= node[1]
        return self.total
