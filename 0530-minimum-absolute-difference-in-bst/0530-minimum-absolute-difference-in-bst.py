# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self._min = inf
        prev = inf
        
        def inorder(node):
            nonlocal prev
            if not node:
                return
            
            inorder(node.left)
            self._min = min(self._min, abs(prev - node.val))
            prev = node.val
            inorder(node.right)
            
        inorder(root)
        
        return self._min