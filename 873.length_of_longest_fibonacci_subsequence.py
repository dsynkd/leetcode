# Similar: "128. Longest Consecutive Sequence"

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        arrSet = set(arr)
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                I = arr[i]
                J = arr[j]
                L = 2
                while I + J in arrSet:
                    # Potential Subsequence detected
                    I,J = J,I+J
                    L += 1
                if L > 2:
                    res = max(res, L)
        return res