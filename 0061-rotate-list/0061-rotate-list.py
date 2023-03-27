# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = head
        n = 0
        while dummy:
            n += 1
            dummy = dummy.next
        factor = k%n
        if not factor:
            return head

        dummy = head
        for _ in range(n - factor - 1):
            dummy = dummy.next
        
        new_head = dummy.next
        temp = new_head
        dummy.next = None
        
        while temp.next:
            temp = temp.next
            
        temp.next = head
        
        return new_head