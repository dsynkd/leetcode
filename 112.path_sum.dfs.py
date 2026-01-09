from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], sum: int) -> bool:
            if not node:
                return False
            sum += node.val
            if not node.left and not node.right:
                return sum == targetSum
            return dfs(node.left, sum) or dfs(node.right, sum)
        
        return dfs(root, 0) if root else False