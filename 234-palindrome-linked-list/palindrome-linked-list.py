# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        newHead=self.reverse(slow.next)
        first=head
        second=newHead
        while second is not None:
            if first.val !=second.val:
                self.reverse(newHead)
                return False
            first=first.next
            second=second.next
        self.reverse(newHead)
        return True
