# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        ans = 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        node = None
        while slow:
            next_node = slow.next
            slow.next = node
            node = slow
            slow = next_node
        
        while node:
            ans = max(ans, node.val + head.val)
            head = head.next
            node = node.next
            
        return ans
        