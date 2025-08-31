class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix) # Rows
        n = len(matrix[0]) # Columns

        for i in range(m):
            v = matrix[i][0]
            j = 1
            while i+j < m and j < n:
                if matrix[i+j][j] != v:
                    return False
                j += 1
        for j in range(1,n):
            v = matrix[0][j]
            i = 1
            while j+i < n and i < m:
                if matrix[i][j+i] != v:
                    return False
                i += 1
        
        return True
