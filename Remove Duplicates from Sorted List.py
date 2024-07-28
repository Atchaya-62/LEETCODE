# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        while a:
            while a.next and a.val==a.next.val:
                a.next=a.next.next
            a=a.next
        return head
        
