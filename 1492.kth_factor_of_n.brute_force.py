class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        for i in range(2, n//2+1):
            if n % i == 0:
                factors.append(i)
        factors.append(n)
        if k > len(factors):
            return -1
        return factors[k-1]