# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = [root]
        depth = 1
        
        while level:
            next_level = []
            for child in level:
                if child.left:
                    next_level.append(child.left)
                    
                if child.right:
                    next_level.append(child.right)
                    
            level = next_level
            if level:
                depth += 1
                
    
        return depth