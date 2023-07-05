# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        info = defaultdict(list)
        
        def dfs(node):
            if not node:
                info[node] = [0, 0]
                return [0, 0]
            
            if node in info:
                return info[node]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            info[node].append(node.val + left[1] + right[1])
            info[node].append(max(left) + max(right))
            
            return info[node]
        
        return max(dfs(root))