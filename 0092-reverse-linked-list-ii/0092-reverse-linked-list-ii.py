# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = head
        arr = []
        ans = []
        
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
            
        ans.extend(arr[:left- 1])
    
        temp = arr[left-1:right]
        temp.reverse()
        ans.extend(temp)
        ans.extend(arr[right:])
    
        prev = None
        if len(ans) > 1:
            prev = ListNode(ans[1])
        head = ListNode(ans[0], prev)
        for i in range(2,len(ans)):
            curr = ListNode(ans[i])
            prev.next = curr
            prev = curr

        return head