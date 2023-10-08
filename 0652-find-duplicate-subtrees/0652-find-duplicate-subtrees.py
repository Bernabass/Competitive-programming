# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        seen = set()
        ans = set()
        ans1 = set()
        
        def dfs(node):
            if not node:
                return ""
            
            left = dfs(node.left)
            right = dfs(node.right)
            traverse = str(node.val) + "right" + right + "left" + left
            if traverse in seen and traverse not in ans1:
                ans.add(node)
                ans1.add(traverse)
                
            seen.add(traverse)
            return traverse
            
            
        dfs(root)
        
        return ans
            