# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr = head
        while curr:
            curr_next = curr.next
            prev = temp
            succ = temp.next
            
            while succ:
                if succ.val > curr.val:
                    break
                prev = succ
                succ = succ.next
                
            curr.next = succ
            prev.next = curr
            curr = curr_next
        
        return temp.next