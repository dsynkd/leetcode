class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if not (m*n == r*c):
            return mat
        res = [[0 for _ in range(c)] for _ in range(r)]
        x,y = 0,0
        for i in range(m):
            for j in range(n):
                res[x][y] = mat[i][j]
                y += 1
                if y == c:
                    y = 0
                    x += 1
        return res