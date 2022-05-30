# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        original=deque()
        while temp:
            original.appendleft(temp.val)
            temp=temp.next
        if len(original)!=0:
            new=ListNode(original[0])
            Reversed=new
            for i in range(1,len(original)):
                Reversed.next=ListNode(original[i])
                Reversed=Reversed.next
            return new
        else:
            return temp