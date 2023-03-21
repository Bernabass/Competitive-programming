# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        odd = head
        ans = odd
        even = head.next
        entn = even
        head = head.next.next
        
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
        
            if not head.next:
                break
            head = head.next.next

        
        odd.next = entn
         
    
        return ans
                
                
            
    