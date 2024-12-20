from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.res = ""

        def dfs(path: list[int], node: Optional[TreeNode]):
            assert(node is not None)
            if node.left is None and node.right is None:
                pathStr = ''.join([chr(a + ord('a')) for a in path][::-1])
                if not self.res or pathStr < self.res:
                    self.res = pathStr
                return
            if node.left:
                dfs(path + [node.left.val], node.left)
            if node.right:
                dfs(path + [node.right.val], node.right)
        
        assert(root is not None)
        dfs([root.val], root)
        return self.res