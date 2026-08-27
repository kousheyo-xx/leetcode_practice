# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail=head
        n=1
        while tail.next:
            n+=1
            tail=tail.next
        k%=n
        if k==0:
            return head
        tail.next=head
        for _ in range(n-k):
            tail=tail.next
        head=tail.next
        tail.next=None
        return head