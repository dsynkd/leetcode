class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []
        m = len(matrix)
        n = len(matrix[0])
        bottom,right,left,top = m-1, n-1, 0, 1
        i,j = 0,0
        direction = 0 if n > 1 else 1
        while len(output) < m * n:
            output.append(matrix[i][j])
            # Right
            if direction == 0:
                j += 1
                if j == right:
                    direction = 1
                    right -= 1
            # Down
            elif direction == 1:
                i += 1
                if i == bottom:
                    direction = 2
                    bottom -= 1
            # Left
            elif direction == 2:
                j -= 1
                if j == left:
                    direction = 3
                    left += 1
            # Top
            elif direction == 3:
                i -= 1
                if i == top:
                    direction = 0
                    top += 1
        return output