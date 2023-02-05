# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        original = deque()
        while dummy:
            original.appendleft(dummy.val)
            dummy = dummy.next
            
        if original:
            new = ListNode(original[0])
            Reversed = new
            for i in range(1,len(original)):
                Reversed.next = ListNode(original[i])
                Reversed = Reversed.next
                
            return new
        else:
            
            return dummy