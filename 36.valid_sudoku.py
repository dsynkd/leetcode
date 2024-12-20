class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = len(board)
        assert(n == len(board[0]))

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        squares = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if num in rows[i]:
                    return False
                else:
                    rows[i].add(num)
                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)
                # Get index of square
                k = (i//3)*3 + j//3
                if num in squares[k]:
                    return False
                else:
                    squares[k].add(num)
        return True