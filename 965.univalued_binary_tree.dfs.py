from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        assert(root)
        def dfs(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)