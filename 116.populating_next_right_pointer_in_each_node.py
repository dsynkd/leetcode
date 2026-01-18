from collections import defaultdict, deque
from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        tree = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if not node:
                continue
            tree[level].append(node)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        
        for level in tree:
            nodes = tree[level]
            for i in range(len(nodes) - 1):
                node = nodes[i]
                node.next = nodes[i+1]
        
        return root