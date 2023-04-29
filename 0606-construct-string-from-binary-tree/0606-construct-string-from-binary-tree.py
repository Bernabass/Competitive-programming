# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node, string):
            if not node:
                return string
            
            string.append(str(node.val))
            if node.left or node.right:
                string.append("(")
                dfs(node.left, string)
                string.append(")")
                
                if node.right:
                    string.append("(")
                    dfs(node.right, string)
                    string.append(")")
                
            return string
        
        return "".join(dfs(root, []))