# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        info = defaultdict(int)
        res = [0]
        
        def dfs(node):
            if not node:
                return 
            
            if node.left:
                info[node] += node.left.val
                
            if node.right:
                info[node] += node.right.val
                
            dfs(node.left)
            dfs(node.right)
            
            if not(node.val % 2):
                res[0] += info[node.left] + info[node.right]
                
            return 
             
        dfs(root)
        return res[0]