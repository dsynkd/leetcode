# Approach: 2D Dynamic Programming, Iterative
# Time Complexity: O(N) where N = n x m
# Space Complexity: O(N)
# Verdict: Pass

import numpy as np

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)+1
        n = len(text2)+1
        cache = np.zeros((m+1,n+1), dtype=int)

        for i in range(1, m):
            for j in range(1, n):
                if text1[i-1] == text2[j-1]:
                    cache[i][j] = cache[i-1][j-1] + 1
                else:
                    cache[i][j] = max(cache[i-1][j], cache[i][j-1])

        return cache[m-1][n-1]
