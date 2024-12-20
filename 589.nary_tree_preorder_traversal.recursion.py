from typing import Optional, Self

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[list[Self]] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: Node) -> list[int]:
        tree = []
        self._preorder(root, tree)
        return tree

    def _preorder(self, root: Optional[Node], tree: list[int]):
        if not root: return
        if root.val is not None:
            tree.append(root.val)
        if root.children:
            for node in root.children:
                self._preorder(node, tree)
