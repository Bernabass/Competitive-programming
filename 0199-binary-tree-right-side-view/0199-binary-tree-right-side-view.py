# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        level, ans = [root], [root.val]
        
        while level:
            next_level = []
            for child in level:
                if child.left:
                    next_level.append(child.left)
                    
                if child.right:
                    next_level.append(child.right)
                    
            if next_level:
                ans.append(next_level[-1].val)
                
            level = next_level
            
            
        return ans