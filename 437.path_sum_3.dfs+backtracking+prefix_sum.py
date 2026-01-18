from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0

        counter = defaultdict(int)
        counter[0] += 1
        def dfs(node, Z):
            if not node:
                return
            Z += node.val
            self.res += counter[Z - k]
            counter[Z] += 1
            dfs(node.left, Z)
            dfs(node.right, Z)
            counter[Z] -= 1
        
        dfs(root, 0)
        return self.res