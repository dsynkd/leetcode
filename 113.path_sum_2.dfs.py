from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        res = []
        path = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            path.append(node.val)
            if not node.right and not node.left:
                if sum(path) == targetSum:
                    res.append(path.copy())
            dfs(node.left)
            dfs(node.right)
            path.pop()

        dfs(root)
        return res