from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []
        q = deque()
        q.append((root, 0))
        
        while q:
            node, h = q.popleft()
            if not node:
                continue
            if len(res) <= h:
                res.append([])
            res[h].append(node.val)
            q.append((node.left, h+1))
            q.append((node.right, h+1))
        
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        
        return res