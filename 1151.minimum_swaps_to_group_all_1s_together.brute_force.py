# Verdict: TLE

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        L = data.count(1)
        res = float('inf')
        
        for i in range(len(data) - L + 1):
            j = i + L
            res = min(res, data[i:j].count(0))

        return res