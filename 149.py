# Approach: Brute Force ?
    # Compute a line (equation parameters m and b) between each pair of points
    # Count how many points lie on each line (predicate y = mx + b)
    # Return the max
# Time Complexity: 
    # Compute a set of all possible pairs of points
        # `O(2 (n \choose 2))`
    # Compute line equations for each pairs of points
        # `O(m) where m is the number of pairs of points`
    # Count number of points that lie on each line
        # `O(m \times n)`
# Space Complexity: ???
# Verdict: Pass
import itertools
import typing
import math
class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        lines = set() # using set to avoid repetition
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