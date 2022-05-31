# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one=[]
        two=[]
        while list1:
            one.append(list1.val)
            list1=list1.next
        while list2:
            two.append(list2.val)
            list2=list2.next
        one.extend(two)
        if one!=[]:
            one.sort()
            head=ListNode(one[0])
            temp=head
            for i in range(1,len(one)):
                head.next=ListNode(one[i])
                head=head.next
            return temp
        return None