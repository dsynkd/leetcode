#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start

import numpy

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = numpy.zeros((m, n))

        def _uniquePaths(i, j):
            if obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if memo[i][j] != 0:
                return memo[i][j]
            if i == 0:
                res = _uniquePaths(i, j-1)
            elif j == 0:
                res = _uniquePaths(i-1, j)
            else:
                res = _uniquePaths(i-1, j) + _uniquePaths(i, j-1)
            memo[i][j] = res
            return memo[i][j]

        res = int(_uniquePaths(m-1, n-1))
        
        return res

# @lc code=end

s = Solution()
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))

