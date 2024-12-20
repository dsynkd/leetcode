class Solution:
    def coinChange(self, coins: list[int], amount: int):
        cache = [0] + ([float('inf')] * amount)

        for coin in coins:
            for i in range(coin, amount + 1):
                cache[i] = min(cache[i], cache[i - coin] + 1)

        if cache[-1] == float('inf'):
            return -1
        
        return cache[-1]