from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        head = res
        n = 0

        # Count non empty linked lists
        for a in lists:
            if a:
                n += 1
        
        while n > 0:

            # Find the minimum head
            m = float('inf')
            mi = 0

            for i in range(len(lists)):
                a = lists[i]
                if a and a.val < m:
                    m = a.val
                    mi = i
            assert(type(m) is int)

            # attach the mimimum to the result and decrement non empty linked list count if necessary
            res.next = ListNode(m)
            res = res.next
            assert(lists[mi] is not None)
            lists[mi] = lists[mi].next
            if lists[mi] is None:
                n -= 1

        return head.next