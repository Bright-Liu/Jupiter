class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        pass


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)

        p1, p2 = dummy1, dummy2
        p = head

        while p:
            if p.val > x:
                p2.next = p
                p2 = p2.next
            else:
                p1.next = p
                p1 = p1.next

        p1.next = dummy2.next
        return dummy1.next
