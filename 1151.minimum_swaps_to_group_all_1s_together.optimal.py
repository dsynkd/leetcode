# Verdict: Accepted

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        L = sum(data)
        swaps = data[:L].count(0)
        res = swaps

        for i in range(1, len(data) - L + 1):
            j = i + L - 1
            if data[i-1] == 0:
                swaps -= 1
            if data[j] == 0:
                swaps += 1
            res = min(res, swaps)

        return res