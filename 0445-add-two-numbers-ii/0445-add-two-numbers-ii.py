# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = sum2 = 0
        i = j = 0
        
        while l1:
            sum1 = sum1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            sum2 = sum2 * 10 + l2.val
            l2 = l2.next
            
        total = sum1 + sum2
        prev = None
        
        while total:
            total, rem = divmod(total, 10)
            curr = ListNode(rem)
            curr.next = prev
            prev = curr
            
        return prev if prev else ListNode(0)