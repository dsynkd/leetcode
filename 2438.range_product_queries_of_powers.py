class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        powers = []
        p = 1
        while p <= n:
            p *= 2
        p //= 2
        while p > 0:
            a = n // p
            if a >= 1:
                powers += [p] * a
            n %= p
            p //= 2
        # sort in non-decreasing order
        powers = powers[::-1]
        res = []
        for i,j in queries:
            a = 1
            for k in range(i,j+1): # j+1 for inclusive range
                a *= powers[k]
            res.append(a % (pow(10,9)+7))
        return res
