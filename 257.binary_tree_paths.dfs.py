# Approach: DFS, pretty simple

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        paths = []

        def dfs(path: str, tree: Optional[TreeNode]):
            assert(tree)
            if tree.left:
                dfs(f'{path}->{tree.left.val}', tree.left)
            if tree.right:
                dfs(f'{path}->{tree.right.val}', tree.right)
            if tree.right is None and tree.left is None: # Leaf Found
                paths.append(path)
        
        assert(root)
        dfs(f'{root.val}', root)
        return paths