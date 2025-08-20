class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        m = len(matrix[0])
        res = [[0 for i in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[j][i] = matrix[i][j]
        return res