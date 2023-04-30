# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        level = [[False, False, root]]
        even_sum = 0
        
        while level:
            next_level = []
            
            for grand_parent, parent, node in level:
                info = [parent, False, node.left]
                
                if grand_parent:
                    even_sum += node.val
            
                if not (node.val % 2):
                    info[1] = True
                     
                if node.left:
                    next_level.append(info.copy())
                    
                if node.right:
                    info[2] = node.right
                    next_level.append(info)
                    
            level = next_level
            
        return even_sum