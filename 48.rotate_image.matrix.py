class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        L = len(matrix)
        for i in range(L):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Invert Horizontally
        for i in range(L):
            for j in range(L//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]