from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# NOTE: A hacker solution: enforce .prev usage.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head.prev = None

        forward_order = []

        while head is not None:
            forward_order.append(head.val)

            if head.next is not None:
                head.next.prev = head
            else:
                # NOTE: head points to the last node when the loop terminates.
                break

            head = head.next

        backward_order = []

        while head is not None:
            backward_order.append(head.val)
            head = head.prev

        return forward_order == backward_order


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # NOTE:
        # 1. Get length.
        # 2. Find "the middle" node.
        # 3. Reverse the first half of the list.
        # 4. Iterate over the first half and the second half.
        # 5. Compare the respective elements as you are iterating.
        #
        # 1 2 5 2 1 -> length = 5 -> middle_node_index = 1 -> the second half = 2 1.
        # 5 8 8 5 -> length = 4 -> middle_node_index = 1 -> the second half = 8 5.
        if head is None:
            return True

        original_head = head
        list_length = 0

        while head is not None:
            list_length += 1
            head = head.next

        if list_length == 1:
            return True

        # NOTE: At this point, list length >= 2.

        middle_node_index = (list_length // 2) - 1
        counter = 0
        head = original_head

        while head is not None:
            if counter == middle_node_index:
                break
            counter += 1
            head = head.next

        middle_node = head

        the_second_half = (
            middle_node.next if list_length % 2 == 0 else middle_node.next.next
        )
        middle_node.next = None
        the_first_half = original_head
        new_the_first_half = self.reverseBabyList(the_first_half)

        return self.areTheSameBabies(new_the_first_half, the_second_half)

    def areTheSameBabies(self, list1, list2) -> bool:
        if not list1 and not list2:
            return True
        if list1 is None:
            return False
        if list2 is None:
            return False

        while list1 is not None and list2 is not None:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next

        return list1 is None and list2 is None

    def reverseBabyList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head

        new_head = self.reverseBabyList(head.next)
        head.next.next = head
        head.next = None
        return new_head


# NOTE: Recursive two pointers.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(current_node):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check(head)
