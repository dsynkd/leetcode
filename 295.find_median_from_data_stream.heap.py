# Identical: [HackerRank] Find the Running Median
# Time Complexity: O(n.log(n)) where we perform a heap push (log(n)) for each element in nums (n)

import heapq

class MedianFinder:

    def __init__(self):
        self.lower = [] # MaxHeap
        self.upper = [] # MinHeap

    def addNum(self, num: int) -> None:
        if not self.lower:
            self.lower.append(-num)
        elif num > -self.lower[0]:
            # if num is bigger than the highest value in lower bound
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        if len(self.lower) > len(self.upper) + 1:
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        elif len(self.upper) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        if len(self.lower) == len(self.upper):
            return (-self.lower[0] + self.upper[0]) / 2
        elif len(self.lower) > len(self.upper):
            return -self.lower[0]
        else:
            return self.upper[0]