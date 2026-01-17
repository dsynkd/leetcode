class Solution:
    def maxCount(self, m: int, n: int, ops: list[list[int]]) -> int:
        for x,y in ops:
            m = min(m, x)
            n = min(n, y)
        return m * n