from typing import Optional, Self

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[list[Self]] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: Node) -> list[int]:
        tree = []
        self._postorder(root, tree)
        return tree

    def _postorder(self, root: Optional[Node], tree: list[int]):
        if not root:
            return
        if root.children:
            for node in root.children:
                self._postorder(node, tree)
        if root.val is not None:
            tree.append(root.val)

