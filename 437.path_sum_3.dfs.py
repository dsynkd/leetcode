from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(tree: Optional[TreeNode], sum: int) -> int:
            if tree is None:
                return 0
            if tree.val == sum:
                return 1 + dfs(tree.left, sum - tree.val) + dfs(tree.right, sum - tree.val)
            return dfs(tree.left, sum - tree.val) + dfs(tree.right, sum - tree.val)

        return dfs(root, targetSum)
    