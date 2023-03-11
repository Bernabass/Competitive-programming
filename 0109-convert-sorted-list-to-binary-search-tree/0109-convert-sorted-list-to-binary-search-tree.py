# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        idx, dummy = 0, head
        while dummy:
            dummy = dummy.next
            idx += 1
        self.head = head
        
        def make_tree(left, right):
            
            if left > right:
                return None
            
            mid = (left+right) // 2
            left = make_tree(left, mid-1)  
            
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = make_tree(mid+1, right)
            
            return root
        
        return make_tree(0, idx-1)