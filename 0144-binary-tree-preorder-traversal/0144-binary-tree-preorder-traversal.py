# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        current = root
        result = []
        while current or stack:
            if current:
                stack.append(current)
                result.append(current.val)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return result