class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        c = 1
        dir = 0
        i = j = 0
        # Limits in the traversal order (Right, Down, Left, Up)
        right,down,left,up = (n-1,n-1,0,0)
        res = [[0 for _ in range(n)] for _ in range(n)]
        while c <= n*n:
            res[i][j] = c
            # Right
            if dir == 0:
                j += 1
                if j == right:
                    dir = 1
                    up += 1
            # Down
            elif dir == 1:
                i += 1
                if i == down:
                    dir = 2
                    right -= 1
            # Left
            elif dir == 2:
                j -= 1
                if j == left:
                    dir = 3
                    down -= 1
            # Up
            elif dir == 3:
                i -= 1
                if i == up:
                    dir = 0
                    left += 1
            c += 1
        return res