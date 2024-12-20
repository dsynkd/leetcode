# Approach: DFS
# Decision version of "113. Path Sum 2"

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(sum: int, tree: Optional[TreeNode]) -> bool:
            if tree is None:
                return False
            sum += tree.val
            if tree.left is None and tree.right is None:
                return sum == targetSum
            return dfs(sum, tree.left) or dfs(sum, tree.right)
        
        return dfs(0, root)