class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


class Solution1:
    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2
        while p1 is not None and p2 is not None:
            if p1.val > p2.next:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next

        if p1 is not None:
            p.next = p1

        if p2 is not None:
            p.next = p2

        return dummy.next
