from functools import cache
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(node, parentRobbed):
            if not node:
                return 0
            if parentRobbed:
                return dfs(node.left, False) + dfs(node.right, False)
            else:
                return max(
                    node.val + dfs(node.left, True) + dfs(node.right, True),
                    dfs(node.left, False) + dfs(node.right, False)
                )
        
        return dfs(root, False)