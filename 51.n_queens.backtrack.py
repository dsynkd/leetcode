from copy import copy, deepcopy
from optparse import Option
from typing import Optional

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        # True = Has Queen, False = Does not have queen
        rows = [False] * n
        cols = [False] * n

        # Stores all solved boards
        self.res = []

        # i = row
        def dfs(i,k):
            if k == n:
                self.res.append(deepcopy(board))
                return
            for j in range(n):
                if rows[i] or cols[j] or board[i][j] == 'Q':
                    continue
                # check positive diagonal upwards
                qFound = False
                a2, b2 = i-1,j+1
                while a2 >= 0 and b2 < n:
                    if board[a2][b2] == 'Q':
                        qFound = True
                        break
                    a2 -= 1
                    b2 +=1
                if qFound:
                    continue

                # check positive diagonal downwards
                qFound = False
                a2, b2 = i+1,j+1
                while a2 < n and b2 < n:
                    if board[a2][b2] == 'Q':
                        qFound = True
                        break
                    a2 += 1
                    b2 +=1
                if qFound:
                    continue
                    
                # check negative diagonal upwards
                qFound = False
                a2, b2 = i-1,j-1
                while a2 >= 0 and b2 >= 0:
                    if board[a2][b2] == 'Q':
                        qFound = True
                        break
                    a2 -= 1
                    b2 -=1
                if qFound:
                    continue

                # check negative diagonal downwards
                qFound = False
                a2, b2 = i+1,j-1
                while a2 < n and b2 >= 0:
                    if board[a2][b2] == 'Q':
                        qFound = True
                        break
                    a2 += 1
                    b2 -=1
                if qFound:
                    continue

                board[i][j] = 'Q'
                rows[i] = True
                cols[j] = True
                dfs(i+1,k+1)
                # Backtrack
                board[i][j] = '.'
                rows[i] = False
                cols[j] = False
        
        dfs(0,0)

        # Convert to according strings
        return [[''.join(row) for row in board] for board in self.res]