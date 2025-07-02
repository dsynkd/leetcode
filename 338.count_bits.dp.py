class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0]
        offset = 1
        for i in range(1,n+1):
            if i == offset * 2:
                offset = i
            dp.append(1 + dp[i-offset])
        return dp