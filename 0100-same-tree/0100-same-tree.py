# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1, tree2 = [], []
        def dfs(node,ans):
            if not node:
                return ans.append(None)
            dfs(node.left,ans)
            dfs(node.right,ans)
            ans.append(node.val)
            return ans
    
        tree1, tree2 = dfs(p,[]), dfs(q,[])
        return tree1 == tree2