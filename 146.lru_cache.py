from typing import Self


class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        
        root = Node(0,0)
        root.next = root
        root.prev = root
        self.head = root
        self.tail = root

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
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
            self._remove(node)
            del self.cache[node.key]
