class MyLinkedList:

    def __init__(self):
        self.nodes = []

    def get(self, index: int) -> int:
        if 0 <= index < len(self.nodes):
            return self.nodes[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.nodes.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.nodes.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= len(self.nodes):
            self.nodes.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < len(self.nodes):
            self.nodes.pop(index)