# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [root]
        ans = [root.val]
        
        while level:
            next_level = []
            curr_max = -inf
            
            for node in level:
                if node.left:
                    next_level.append(node.left)
                    curr_max = max(curr_max, node.left.val)
                    
                if node.right:
                    next_level.append(node.right)
                    curr_max = max(curr_max, node.right.val)
                    
            if curr_max != -inf:
                ans.append(curr_max)
                
            level = next_level
            
        return ans
        