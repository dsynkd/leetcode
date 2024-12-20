from copy import deepcopy
from typing import Optional
import numpy

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        assert(n == len(board[0]))

        # Use sets to avoid creating faulty combinations
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]

        # Update rows/cols/squares based on given board
        # (Also convert to integer in the meantime for better performance)
        for i in range(n):
            for j in range(n):
                c = board[i][j]
                k = (i//3)*3 + j//3
                if c == '.':
                    board[i][j] = 0
                else:
                    c = int(c)
                    board[i][j] = c
                    rows[i].add(c)
                    cols[j].add(c)
                    squares[k].add(c)

        # DFS until we have a valid board
        def dfs(i: int, j: int) -> Optional[list[list[str]]]:
            assert(j < n)
            if i == n:
                return deepcopy(board)
            if board[i][j]:
                if j == n-1:
                    return dfs(i+1, 0)
                else:
                    return dfs(i, j+1)
            for a in range(1, 10):
                if a in rows[i]:
                    continue
                if a in cols[j]:
                    continue
                k = (i//3)*3 + j//3
                if a in squares[k]:
                    continue
                board[i][j] = a
                rows[i].add(a)
                cols[j].add(a)
                squares[k].add(a)
                res = None
                if j == n-1:
                    res = dfs(i+1, 0)
                else:
                    res = dfs(i, j+1)
                if res:
                    return res
                # Backtrack
                board[i][j] = 0
                rows[i].remove(a)
                cols[j].remove(a)
                squares[k].remove(a)
            return None

        res = dfs(0,0)
        assert(res is not None)

        for i in range(n):
            for j in range(n):
                board[i][j] = str(res[i][j])