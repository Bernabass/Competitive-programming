# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            list1=[head.val]
            while head:
                if head.val!=list1[-1]:
                    list1.append(head.val)
                head=head.next
            head=ListNode(list1[0])
            temp=head
            for i in range(1,len(list1)):
                head.next=ListNode(list1[i])
                head=head.next
            return temp
        return None     