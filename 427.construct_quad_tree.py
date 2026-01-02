from typing import Self


class Node:
    def __init__(self, val: int, isLeaf: bool, topLeft: Self | None = None, topRight: Self | None = None, bottomLeft: Self | None = None, bottomRight: Self | None = None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        n = len(grid)

        def dfs(y1, y2, x1, x2):
            L = x2 - x1
            if L <= 1:
                return Node(grid[x1][y1], True)

            topLeft = dfs(y1, y2 - (L//2), x1, x2 - L//2)
            topRight = dfs(y1 + L//2, y2, x1, x2 - L//2)
            bottomLeft = dfs(y1, y2 - L//2, x1 + L//2, x2)
            bottomRight = dfs(y1 + L//2, y2, x1 + L//2, x2)

            if ((topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf) and
                (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val)):
                return Node(topLeft.val, True)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        return dfs(0,n,0,n)
