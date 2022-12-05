# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            return node.val + dfs(node.right) + dfs(node.left)
        def calc(node):
            return abs(dfs(node.left)- dfs(node.right))
        def find_tilt(node):
            if not node:
                return 0
            return calc(node) + find_tilt(node.right) + find_tilt(node.left)
        return find_tilt(root)