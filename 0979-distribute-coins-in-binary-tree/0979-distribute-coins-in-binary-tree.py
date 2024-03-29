# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        min_moves = [0]
        
        def dfs(node):
            if not node:
                return 0
            
            node.val += dfs(node.left)
            node.val += dfs(node.right)
            
            min_moves[0] += abs(1 - node.val)
            
            return node.val - 1
        
        dfs(root)
        
        return min_moves[0]
            
            
            
            
        
            
        