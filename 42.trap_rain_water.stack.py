from collections import deque

class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        s = deque()
        
        for i in range(n):
            while s and height[i] > height[s[-1]]:
                l = s.pop()
                if not s:
                    break
                d = i - s[-1] - 1
                h = min(height[i], height[s[-1]]) - height[l]
                res  += d * h
            s.append(i)
        return res