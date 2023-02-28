# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = ListNode()
        temp.next = head

        left, right = temp, head
        for _ in range(n):
            right = right.next

        while right:
            left, right = left.next, right.next
        
        left.next = left.next.next
        
        return temp.next