# Approach:
# 1. preorder[0] is always the root node
# 2. looking for the root node in inorder will give us the pivot point where
# we can split right and left subtrees
# Verdict: Pass

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        tree = TreeNode()
        self._buildTree(tree, preorder, inorder)
        return tree

    def _buildTree(self, root: TreeNode, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        L = len(inorder)
        assert(L == len(preorder))
        root.val = preorder[0]
        i = 0
        while inorder[i] != root.val:
            i += 1
        left_preorder = preorder[1:i+1]
        left_inorder = inorder[0:i]
        right_preorder = preorder[i+1:L]
        right_inorder = inorder[i+1:L]
        if left_inorder or left_preorder:
            root.left = TreeNode()
            self._buildTree(root.left, left_preorder, left_inorder)
        if right_inorder or right_preorder:
            root.right = TreeNode()
            self._buildTree(root.right, right_preorder, right_inorder)