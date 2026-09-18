# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        
        slow=head
        fast=head.next

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        left=self.sortList(head)
        right=self.sortList(second)

        return self.merge(left,right)

    def merge(self,left,right):
        dummy=ListNode(0)
        temp=dummy

        while left is not None and right is not None:
            if left.val <= right.val:
                temp.next=left
                left=left.next

            else:
                temp.next=right
                right=right.next
            
            temp=temp.next

        if left is not None:
            temp.next=left
        else:
            temp.next=right
        
        return dummy.next

            

        
    