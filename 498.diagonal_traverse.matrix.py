class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        diag = True # True = positive diagonal, False = negative diagonal
        i = j = 0
        m, n = len(mat), len(mat[0])
        res = []
        while len(res) < n*m:
            res.append(mat[i][j])
            if diag:
                if i == 0 or j ==  n-1:
                    diag = not diag
                    if j == n-1:
                        i += 1
                    elif i == 0:
                        j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 or i == m-1:
                    diag = not diag
                    if i == m-1:
                        j += 1
                    elif j == 0:
                        i += 1
                else:
                    i += 1
                    j -= 1
        return res