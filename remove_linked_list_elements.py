from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# NOTE: Recursive.
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if head is None:
#             return None
#         if head.val == val:
#             return self.removeElements(head.next, val)
#
#         head.next = self.removeElements(head.next, val)
#         return head


# NOTE: Iterative.
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        if head is None:
            return None

        c = head
        p = head

        while c is not None:
            if c.val == val:
                p.next = c.next
            else:
                p = c
            c = c.next

        return head
