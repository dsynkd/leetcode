from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> list[int]:
            if not node:
                return [0,0]
            l = dfs(node.left)
            r = dfs(node.right)
            # a = with root, b = without root
            a = node.val + l[1] + r[1]
            b = max(l) + max(r)
            return [a,b]
        
        return max(dfs(root))