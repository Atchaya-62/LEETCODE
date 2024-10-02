# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(0)
        prev=temp
        while head:
            next=head.next
            if prev.val>=head.val:
                prev=temp

            while prev.next and prev.next.val<head.val:
                prev=prev.next

            head.next=prev.next
            prev.next=head
            head=next

        return temp.next
        
