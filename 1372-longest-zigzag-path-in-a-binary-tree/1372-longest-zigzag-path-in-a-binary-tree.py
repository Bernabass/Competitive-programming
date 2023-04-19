# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def zigzag(root, right, total):
            if not root:
                return total
            
            left = zigzag(root.left, 0, total+1 if right else 1)
            right = zigzag(root.right, 1, total+1 if not right else 1)

            return max(left, right)
        
        return zigzag(root, None, 0) - 1
            
            
            
            
            
            
                
            