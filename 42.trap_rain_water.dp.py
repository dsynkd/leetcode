class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        lmax,rmax = [0] * n, [0] * n
        
        m = 0
        for i in range(n):
            m = max(m, height[i])
            lmax[i] = m

        m = 0
        for i in range(n-1,-1,-1):
            m = max(m, height[i])
            rmax[i] = m

        for i in range(1, len(height)-1):
            h = height[i]
            l = lmax[i]
            r = rmax[i]
            diff = min(l,r) - h 
            res += diff
        
        return res