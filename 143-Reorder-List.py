# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if fast:
            prev=slow
            slow=slow.next
        prev.next=None
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        temp=head
        while temp and prev:
            temp1=temp.next
            temp2=prev.next
            temp.next=prev
            prev.next=temp1
            temp=temp1
            prev=temp2
