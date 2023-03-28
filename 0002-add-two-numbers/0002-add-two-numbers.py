# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        have = 0
        head = ListNode()
        ans = head
        while l1 or l2 or have:
            curr_sum = have
            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
                
            have = curr_sum // 10
            new_val = curr_sum % 10
            
            head.next = ListNode(new_val)
            head = head.next
        
        return ans.next