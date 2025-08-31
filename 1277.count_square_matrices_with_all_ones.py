class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def isOneMatrix(i1,j1,i2,j2):
            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    if matrix[i][j] != 1:
                        return False
            return True
        
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    res += 1
                    i2 = i + 1
                    j2 = j + 1
                    while i2 < m and j2 < n:
                        if isOneMatrix(i,j,i2,j2):
                            res += 1
                        i2 = i2 + 1
                        j2 = j2 + 1
        
        return res