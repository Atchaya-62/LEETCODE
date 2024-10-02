# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev=head
        temp=head
        for i in range(n):
            temp=temp.next
        if not temp:
            return head.next

        while temp.next:
            prev=prev.next
            temp=temp.next
        prev.next=prev.next.next
        
        return head
