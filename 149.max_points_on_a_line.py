import itertools
import math

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        lines = set()
        for ((x1,y1), (x2,y2)) in itertools.combinations(points, 2):
            if x1 == x2:
                m = math.inf
                b = x1
            else:
                m = (y2-y1)/(x2-x1)
                b = y2 - (m * x2)
            lines.add((m,b))

        r = 1
        for (m,b) in lines:
            c = 0
            for (x,y) in points:
                if m == math.inf and b == x:
                    c += 1
                elif math.isclose(m*x + b, y):
                    c += 1
                if c > r:
                    r = c

        return r