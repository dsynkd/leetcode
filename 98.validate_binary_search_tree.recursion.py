# Approach: Depth First Search
# Verdict: Pass

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self._isValidBST(root, float('-inf'), float('inf'))
    
    def _isValidBST(self, root: Optional[TreeNode], lowerBound: float, upperBound: float) -> bool:
        if root is None:
            return True
        if root.val >= upperBound or root.val <= lowerBound:
            return False
        return self._isValidBST(root.left, lowerBound, root.val) and self._isValidBST(root.right, root.val, upperBound)