from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
        elif root2:
            node = TreeNode(root2.val)
            node.left = self.mergeTrees(None, root2.left)
            node.right = self.mergeTrees(None, root2.right)
        elif root1:
            node = TreeNode(root1.val)
            node.left = self.mergeTrees(None, root1.left)
            node.right = self.mergeTrees(None, root1.right)
        else:
            return None
        return node