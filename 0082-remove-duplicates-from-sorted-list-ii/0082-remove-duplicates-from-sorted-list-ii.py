# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq = defaultdict(int)
        org = head
        while head:
            freq[head.val] += 1
            head = head.next
         
        new_head = None
        ans = new_head
        
        while org:
            if freq[org.val] == 1:
                if new_head:
                    new_head.next = ListNode(org.val)
                    new_head = new_head.next
                    
                else:
                    new_head = ListNode(org.val)
                    ans = new_head
            
            org = org.next
            
        return ans