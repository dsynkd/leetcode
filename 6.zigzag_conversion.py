class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        i = 0
        grid = [[''] * len(s) for _ in range(numRows)]

        for c in range(len(s)): # column index
            if i >= len(s):
                break

            mod = c % (numRows-1)

            if mod == 0:
                for r in range(numRows):
                    if i >= len(s): break
                    grid[r][c] = s[i]
                    i += 1
            else:
                mod = (numRows-1) - mod
                grid[mod][c] = s[i]
                i += 1

        o = ''
        for r in grid:
            o += ''.join(r)
        return o