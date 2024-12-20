# Approach: DFS
# Similar to "257. Binary Tree Paths"
# Make sure to copy the path arg, since python is pass by reference

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        paths = []

        def dfs(path: list[int], tree: Optional[TreeNode]):
            if tree is None:
                return
            path += [tree.val]
            if tree.right is None and tree.left is None: # Leaf Found
                if sum(path) == targetSum:
                    paths.append(path)
            dfs(path[:], tree.left)
            dfs(path[:], tree.right)

        dfs([], root)
        return paths