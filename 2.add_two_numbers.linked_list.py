from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ''
        b = ''
        while l1:
            a += str(l1.val)
            l1 = l1.next
        while l2:
            b += str(l2.val)
            l2 = l2.next
        res = int(a[::-1]) + int(b[::-1])
        
        root = ListNode()
        node = root
        for c in str(res)[::-1]:
            node.next = ListNode(int(c))
            node = node.next
        return root.next