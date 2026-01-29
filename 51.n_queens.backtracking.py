from copy import copy, deepcopy
from optparse import Option
from typing import Optional

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        # True = Has Queen, False = Does not have queen
        rows = [False] * n
        cols = [False] * n
        pos_diag = [False] * (n*2-1)
        neg_diag = [False] * (n*2-1)
        self.res = []

        # i = row, k = number of queens on the board
        def dfs(i,k):
            if k == n:
                self.res.append(deepcopy(board))
                return
            for j in range(n):
                if rows[i] or cols[j] or board[i][j] == 'Q' or pos_diag[i+j] or neg_diag[n-j-1+i]:
                    continue
                board[i][j] = 'Q'
                rows[i] = cols[j] = pos_diag[i+j] = neg_diag[n-j-1+i] = True
                dfs(i+1,k+1)
                # Backtrack
                board[i][j] = '.'
                rows[i] = cols[j] = pos_diag[i+j] = neg_diag[n-j-1+i] = False
        
        dfs(0,0)

        # Convert to according strings
        return [[''.join(row) for row in board] for board in self.res]