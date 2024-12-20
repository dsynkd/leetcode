from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        self._inorder(root, tree)
        return tree

    def _inorder(self, root: Optional[TreeNode], tree: list[int]):
        if not root: return
        self._inorder(root.left, tree)
        tree.append(root.val)
        self._inorder(root.right, tree)