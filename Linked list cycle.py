# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h=head
        temp=head
        while temp and temp.next:
            h=h.next
            temp=temp.next.next
            if h==temp:
                return True
        return False
