# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next 
                
        head = node = ListNode(None) 
        values.sort()
        for val in values:
            node.next = ListNode(val)
            node = node.next 
            
        return head.next