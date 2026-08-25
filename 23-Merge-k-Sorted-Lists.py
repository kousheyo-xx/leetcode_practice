# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)<2:
            return lists[0] if lists else None
        while len(lists)>=2:
            merged=[]
            for i in range(0,len(lists),2):
                list1=lists[i]
                list2=lists[i+1] if i+1<len(lists) else None
                merged.append(self.merge(list1,list2))
            lists=merged
        return merged[0]
    def merge(self,list1,list2):
        dummy=ListNode(0,None)
        temp=dummy
        while list1 and list2:
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        temp.next=list1 if list1 else list2
        return dummy.next


