# Approach: Brute Force
# Verdict: Wrong (WIP)

from copy import deepcopy
import numpy as np


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = int(matrix[0][0])
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + int(matrix[i][j])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + int(matrix[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + int(matrix[i][j]) + int(matrix[i-1][j]) + int(matrix[i][j-2])
        print(np.array(dp))
        return res