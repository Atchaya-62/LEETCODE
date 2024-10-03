# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        temp=head
        while temp and temp.next:
            h=h.next
            temp=temp.next.next
            if h==temp:
                h=head
                while h!=temp:
                    h=h.next
                    temp=temp.next
                return h
        return None
        
