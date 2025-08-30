class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m,n = len(matrix), len(matrix[0])
        i = j = 0
        # Direction
        d = 0 if n > 1 else 1 # Start downwards if there is only 1 column
        # Limits in the traversal order (Right, Down, Left, Up)
        right,down,left,up = (n-1,m-1,0,0)
        output = []

        while len(output) < m * n:
            output.append(matrix[i][j])
            # Right
            if d == 0:
                j += 1
                if j == right:
                    d = 1
                    up += 1
            # Down
            elif d == 1:
                i += 1
                if i == down:
                    d = 2
                    right -= 1
            # Left
            elif d == 2:
                j -= 1
                if j == left:
                    d = 3
                    down -= 1
            # Up
            elif d == 3:
                i -= 1
                if i == up:
                    d = 0
                    left += 1
        return output