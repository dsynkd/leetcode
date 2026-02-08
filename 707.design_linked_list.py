class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        node = Node(-1)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node

    def get(self, index: int) -> int:
        node = self.head.next
        for i in range(index):
            node = node.next
            if node.val == -1:
                return -1
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.head
        for i in range(index):
            node = node.next
            if node.val == -1:
                return
        newNode = Node(val)
        newNode.prev = node
        newNode.next = node.next
        node.next.prev = newNode
        node.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        node = self.head.next
        for i in range(index):
            node = node.next
            if node.val == -1:
                return
        node.next.prev = node.prev
        node.prev.next = node.next
