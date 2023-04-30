# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        even_sum = [0]
        
        def dfs(child, parent, grandParent):
            
            if not(child):
                return 0
            
            if grandParent and not(grandParent.val % 2):
                even_sum[0] += child.val
                
            dfs(child.left, child, parent)
            dfs(child.right, child, parent)
            
        dfs(root, None, None)
            
        return even_sum[0]