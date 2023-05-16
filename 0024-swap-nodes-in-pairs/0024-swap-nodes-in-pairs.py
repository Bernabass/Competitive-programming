# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not (head and head.next):
            return head
        
        curr = head
        adj = head.next
        temp = adj.next
        
        adj.next = curr
        curr.next = self.swapPairs(temp)
        
        return adj