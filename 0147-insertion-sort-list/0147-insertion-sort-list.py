# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr_node = head
        
        while curr_node:
            prev_node = temp
            while prev_node.next and prev_node.next.val < curr_node.val:
                prev_node = prev_node.next
                
            next_node = curr_node.next
            curr_node.next = prev_node.next
            prev_node.next = curr_node
            curr_node = next_node
        
        return temp.next