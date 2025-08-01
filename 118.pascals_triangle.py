class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        prevRow = [1]
        res = [[1]]
        for i in range(1,numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = prevRow[j-1] + prevRow[j]
            res.append(row)
            prevRow = row
        return res