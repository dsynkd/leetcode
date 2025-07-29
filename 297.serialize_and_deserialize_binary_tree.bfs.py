from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ''
        q = deque([root])
        res = f'{root.val}.'

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
                res += f'l{node.left.val}.'
            else:
                res += 'l.'

            if node.right:
                q.append(node.right)
                res += f'r{node.right.val}.'
            else:
                res += 'r.'

        return res
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        # Extract root value
        i = 0
        token = ''
        while data[i] != '.':
            token += data[i]
            i += 1
        root = TreeNode(int(token))

        # Uses queue to keep track of currently populating node
        path = deque([root])
        i += 1

        while i < len(data):
            node = path.popleft()
            assert(data[i] == "l")
            # Extract left node
            token = ''
            i += 1
            while data[i] != '.':
                token += data[i]
                i += 1
            if token:
                node.left = TreeNode(int(token))
                path.append(node.left)
            i += 1
            # Extract right node
            assert(data[i] == "r")
            token = ''
            i += 1
            while data[i] != '.':
                token += data[i]
                i += 1
            if token:
                node.right = TreeNode(int(token))
                path.append(node.right)
            i += 1
        
        return root