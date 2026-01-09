from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return int(1e6)
            if not node.left and not node.right:
                return depth
            return min(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        
        return dfs(root, 1) if root else 0