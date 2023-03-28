# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        dummy = head
        while dummy:
            arr.append(dummy.val)
            dummy = dummy.next
        
        ans, n = 0, len(arr)

        for idx in range(n // 2):
            ans = max(ans, arr[idx] + arr[n-idx-1])
            
        return ans
        