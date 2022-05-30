# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output=ListNode()
        size=0
        count=0
        temp=head
        new=head
        while temp:
            size+=1
            temp=temp.next
        while new:
            count+=1
            if count==(size//2)+1:
                s=new
                break
            new=new.next
        return s 