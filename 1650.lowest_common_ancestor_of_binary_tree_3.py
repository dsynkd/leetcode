class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        pa = set()
        while p:
            pa.add(p.val)
            p = p.parent
        while q:
            if q.val in pa:
                return q
            q = q.parent
        # Should never get to this point
        assert(False)