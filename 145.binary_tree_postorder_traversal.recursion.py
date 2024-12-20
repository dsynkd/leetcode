from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = []
        self._postorder(root, tree)
        return tree

    def _postorder(self, root: Optional[TreeNode], tree: list[int]):
        if not root: return
        self._postorder(root.left, tree)
        self._postorder(root.right, tree)
        tree.append(root.val)