class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        N = len(weights)

        def can(cap):
            i = 0
            c = 0
            s = 0
            while i < N and c < days:
                if s + weights[i] > cap:
                    c += 1
                    s = 0
                else:
                    s += weights[i]
                    i += 1
            return i == N
        
        i, j = min(weights), sum(weights)
        while i <= j:
            m = i + (j - i) // 2
            if can(m):
                j = m - 1
            else:
                i = m + 1
        
        return i