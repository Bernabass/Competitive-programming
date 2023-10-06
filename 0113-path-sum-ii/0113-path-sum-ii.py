# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def dfs(node, target):
            if not node:
                return []
            
            if not (node.left or node.right):
                if node.val == target:
                    return [deque([node.val])]
                
                return []
            
            ans = []
            left = dfs(node.left, target - node.val)                
            right = dfs(node.right, target - node.val)
            
            for val in left:
                val.appendleft(node.val)
                ans.append(val)
                
            for val in right:
                val.appendleft(node.val)
                ans.append(val)
            
            return ans
        
        return dfs(root, targetSum)