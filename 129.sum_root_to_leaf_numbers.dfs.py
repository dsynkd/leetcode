from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def dfs(path: str, node: Optional[TreeNode]):
            if not node:
                return
            path += str(node.val)
            if node.left is None and node.right is None:
                self.sum += int(path)
                return
            dfs(path, node.left)
            dfs(path, node.right)
        
        dfs("", root)
        return self.sum