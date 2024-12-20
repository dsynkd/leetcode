class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1list = []
        l2list = []
        while l1 is not None:
            l1list.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2list.append(l2.val)
            l2 = l2.next
        l1list.reverse()
        l2list.reverse()
        l1num = int(''.join(str(e) for e in l1list ))
        l2num = int(''.join(str(e) for e in l2list ))
        r = l1num + l2num
        sl = str(r)[::-1]
        rs = ListNode()
        p = rs
        for s in sl:
            rs.next = ListNode()
            rs.next.val = int(s)
            rs = rs.next
        return p.next