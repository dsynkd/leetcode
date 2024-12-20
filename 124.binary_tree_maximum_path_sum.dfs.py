# Approach: Depth First Search (DFS)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        assert(root)
        self.max = root.val
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            val = node.val
            leftVal = max(0, dfs(node.left))
            rightVal = max(0, dfs(node.right))
            self.max = max(self.max, val + leftVal + rightVal)
            return val + max(leftVal, rightVal)

        _ = dfs(root)
        return self.max