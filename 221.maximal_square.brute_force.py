# Approach: Brute Force
# Verdict: TLE

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    continue
                A = i+2
                B = j+2
                L = 1 # Length of matrix of 1s
                isOneMatrix = True
                while A < m and B < n:
                    # Check if we have a "A x B" matrix of 1s, starting with 2x2
                    for x in range(i, A):
                        for y in range(j, B):
                            if matrix[x][y] == "0":
                                isOneMatrix = False
                    if not isOneMatrix:
                        break
                    # Increment Length and potential dimensions if matrix of 1s is verified
                    A += 1
                    B += 1
                    L += 1
                res = max(res, L*L)
        return res
