class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        N = len(piles)

        def can(k):
            i = 0
            c = 0
            
            while i < N and c <= h:
                c += (piles[i]-1) // k + 1
                i += 1
            
            return i == N and c <= h
        
        i, j = 1, max(piles)
        while i <= j:
            m = i + (j - i) // 2
            if can(m):
                j = m - 1
            else:
                i = m + 1
        
        return i