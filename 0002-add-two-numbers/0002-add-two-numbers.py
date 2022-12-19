# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp, temp2 = ListNode(l1.val,l1.next), ListNode(l2.val,l2.next)
        x, x2 = None, None
        s, s2 = '', ''
        while temp:
            l1.next = x
            x = l1
            temp = temp.next
            if temp:l1 = ListNode(temp.val,temp.next)
        while temp2:
            l2.next = x2
            x2 = l2
            temp2 = temp2.next
            if temp2:l2 = ListNode(temp2.val,temp2.next)
        while l1:
            s += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        res = list(map(int,str(eval(s+"+"+s2))))
        res.reverse()
        def insert(root, item): 
            temp = ListNode(0) 
            temp.val = item 
            temp.next = root 
            root = temp
            return root 
        def arrayToList(arr, n): 
            root = None 
            for i in range(n - 1, -1, -1): 
                root = insert(root, arr[i])
            return root 
        return arrayToList(res,len(res))