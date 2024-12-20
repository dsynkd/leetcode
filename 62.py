#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[0]*n for i in range(m)]

        def _uniquePaths(m, n):
            if m == 0 or n == 0:
                return 1
            if memo[m][n] != 0:
                return memo[m][n]
            memo[m][n] = _uniquePaths(m-1, n) + _uniquePaths(m, n-1)
            return memo[m][n]

        return _uniquePaths(m-1, n-1)
        
# @lc code=end

