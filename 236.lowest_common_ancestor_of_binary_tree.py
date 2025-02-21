class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return
            if node in (p,q):
                return node
            
            l = dfs(node.left)
            r = dfs(node.right)

            if l and r:
                return node
            return l or r
        
        res = dfs(root)
        assert(res)
        return res