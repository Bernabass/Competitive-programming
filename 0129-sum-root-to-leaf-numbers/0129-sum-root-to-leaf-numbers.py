# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = [0]
        def add(node, prev_sum):
            if not node.left and not node.right:
                prev_sum = prev_sum * 10 + node.val
                total[0] += prev_sum
                return
            
            if node.left:
                add(node.left, prev_sum * 10 + node.val)
            
            if node.right:
                add(node.right,prev_sum * 10 + node.val)
            
            return
        
        add(root, 0)   
        return total[0]