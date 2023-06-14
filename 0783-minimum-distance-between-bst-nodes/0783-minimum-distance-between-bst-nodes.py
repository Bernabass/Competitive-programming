# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        ans, prev = inf, inf
        
        def dfs(node):
            nonlocal ans, prev
            if not node: return
            
            dfs(node.left)
            ans, prev = min(ans, abs(prev - node.val)), node.val
            dfs(node.right)
            
        dfs(root)
        return ans