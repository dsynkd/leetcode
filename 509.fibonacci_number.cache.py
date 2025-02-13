class Solution:
    cache = dict()
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.cache:
            return self.cache[n]
        fib1 = self.fib(n-1)
        self.cache[n-1] = fib1
        fib2 = self.fib(n-2)
        self.cache[n-2] = fib2
        return fib1 + fib2