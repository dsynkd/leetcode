class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        res = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                # get the max
                m = 0
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        m = max(m, grid[a][b])
                res[i][j] = m
        return res