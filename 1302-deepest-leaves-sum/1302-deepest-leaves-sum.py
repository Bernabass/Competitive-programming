# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        total = 0
        level = [root]
        
        while level:
            next_level = []
            
            for child in level:
                if child.left:
                    next_level.append(child.left)
                
                if child.right:
                    next_level.append(child.right)
                    
                
            if not next_level:
                for node in level:
                    total += node.val
                    
            level = next_level
            
        return total