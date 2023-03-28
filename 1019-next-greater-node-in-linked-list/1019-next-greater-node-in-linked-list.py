# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, ans = [], []
        i = 0
        while head:
            ans.append(0)
            curr = head.val
            while stack and curr > stack[-1][0].val:
                popped = stack.pop()
                val, idx = popped[0], popped[1]
                ans[idx] = curr
                
            stack.append((head, i))
            head = head.next
            i += 1
            
        return ans