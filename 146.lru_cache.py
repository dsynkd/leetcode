from typing import Self


class Node:
    
    next: Self | None
    prev: Self | None

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        
        # Sentinel Nodes
        self.head = self.tail = Node(0,0)
        self.head.prev = self.tail
        self.tail.next = self.head

    def _remove(self, node: Node):
        assert(node.prev and node.next) # We can make this assertion because of dummy nodes
        node.prev.next, node.next.prev = node.next, node.prev

    def _append(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        assert(self.head.next) # Dummy node assertion again
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._append(node)
            node.value = value
            return
        
        node = Node(key, value)
        self.cache[key] = node
        self._append(node)

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            assert(node) # Dummy node again
            self._remove(node)
            del self.cache[node.key]
