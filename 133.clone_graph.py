from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        
        visited = dict()

        def _clone(oldNode: Node) -> Node:
            val = oldNode.val
            newNode = Node(val)
            visited[val] = newNode
            newNeighbors = []
            for neighbor in oldNode.neighbors:
                if neighbor.val in visited:
                    newNeighbors.append(visited[neighbor.val])
                else:
                    newNeighbors.append(_clone(neighbor))
            newNode.neighbors = newNeighbors
            return newNode
        
        if node is None:
            return None

        return _clone(node)