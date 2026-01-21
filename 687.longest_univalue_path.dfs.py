from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0
        def dfs(node, parent):
            if not node:
                return 0
            l = dfs(node.left, node)
            r = dfs(node.right, node)
            self.res = max(self.res, l + r)
            if parent and node.val == parent.val:
                return max(l,r) + 1
            return 0
        
        dfs(root, None)
        return self.res