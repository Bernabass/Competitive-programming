# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        child = TreeNode(val)
        if not root:
            return child
    
        node = root
        left = 1
        while node :
            prev = node
            if val < node.val:
                node = node.left
                left = 1
                
            else:
                node = node.right
                left = 0
          
        
        if left:
            prev.left = child
        
        else:
            prev.right = child
            
        return root  