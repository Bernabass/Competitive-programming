# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = head
        temp = [dummy.val]
        ans = []
        
        while dummy:
            dummy = dummy.next
            if dummy:
                temp.append(dummy.val)
                
        for idx, val in enumerate(temp):
            if val < x:
                ans.append(val)
                temp[idx] = 101
                
        for val in temp:
            if val != 101:
                ans.append(val)
        prev = None
        if len(ans) > 1:
            prev = ListNode(ans[1])
        head = ListNode(ans[0], prev)
        for i in range(2,len(ans)):
            curr = ListNode(ans[i])
            prev.next = curr
            prev = curr
            
        return head       