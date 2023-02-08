# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        flag = True
        
        for i in lists:
            dummy, stage = i, deque()
            while dummy:
                stage.append(dummy.val)
                dummy = dummy.next
                
            if stage:
                flag = False
            arr.append(stage)
           
        if not arr or flag:
            return None
            
        for i in range(1,len(lists)):
            merged = deque()
            curr, prev = arr[i], arr[i-1]
            
            while curr and prev:
                if curr[0] <= prev[0]:
                    merged.append(curr.popleft())
                else:
                    merged.append(prev.popleft())
            
            if curr:
                while curr:
                    merged.append(curr.popleft())
                    
            if prev:
                while prev:
                    merged.append(prev.popleft())
            
            arr[i] = merged
          
        ans = arr[-1]
        prev = None
        if len(ans) > 1:
            prev = ListNode(ans[1])
        head = ListNode(ans[0], prev)
        for i in range(2,len(ans)):
            curr = ListNode(ans[i])
            prev.next = curr
            prev = curr
            
        return head