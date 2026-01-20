from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return -1
            leftDiameter = dfs(node.left)
            rightDiameter = dfs(node.right)
            self.res = max(self.res, leftDiameter + rightDiameter + 2)
            return max(leftDiameter, rightDiameter) + 1
        
        dfs(root)
        return self.res