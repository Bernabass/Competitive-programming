# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ans, temp = [], deque()
        dummy = head
        
        while dummy:
            temp.append(dummy.val)
            dummy = dummy.next
            
        while temp:
            stage = deque()
            count = len(temp)
            for _ in range(k):
                if temp:
                    if count >= k:
                        stage.appendleft(temp.popleft())
                    else:
                        stage.append(temp.popleft()) 
            ans.extend(stage)
            
        prev = None
        if len(ans) > 1:
            prev = ListNode(ans[1])
        head = ListNode(ans[0], prev)
        
        for i in range(2,len(ans)):
            curr = ListNode(ans[i])
            prev.next = curr
            prev = curr

        return head 