from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        res = 0
        while q:
            (node, depth) = q.popleft()
            if not node:
                res = max(res, depth)
                continue
            q.append((node.left, depth+1))
            q.append((node.right, depth+1))
        return res