# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        targets = {p, q}
        
        def dfs(node):
            if not node:
                return set()
            
            ans = set()
            if node in targets:
                ans.add(node)
                
            ans = ans.union(dfs(node.left))
            ans = ans.union(dfs(node.right))
            
            if ans == targets:
                return {node}
            
            return ans
            
        return dfs(root).pop()
            