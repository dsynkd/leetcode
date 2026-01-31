class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefixSum = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(m):
                self.prefixSum[i][j+1] = self.prefixSum[i][j] + matrix[i-1][j]
        
        for i in range(n):
            for j in range(m+1):
                self.prefixSum[i+1][j] += self.prefixSum[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2+1][col2+1] - self.prefixSum[row1][col2+1] - self.prefixSum[row2+1][col1] + self.prefixSum[row1][col1]
