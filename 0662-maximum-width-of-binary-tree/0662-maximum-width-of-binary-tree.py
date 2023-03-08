# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        max_width = 1
        level = [(root, 1)]
        
        while level:
            next_level = []
   
            for child, position in level:
                if child.left: 
                    next_level.append((child.left, 2*position))
                    
                if child.right:
                    next_level.append((child.right, 2*position+1))
                    
            level = next_level
            if level:
                max_width = max(max_width, level[-1][1] - level[0][1] + 1)
                
            
            
        return max_width
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 