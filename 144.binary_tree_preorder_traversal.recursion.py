from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        self._preorder(root, tree)
        return tree

    def _preorder(self, root: Optional[TreeNode], tree: list[int]):
        if not root: return
        tree.append(root.val)
        self._preorder(root.left, tree)
        self._preorder(root.right, tree)