# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.changed1 = None
        self.changed2 = None
        self.org = TreeNode(float('-inf'))
        self.iot(root)
        self.changed1.val , self.changed2.val = self.changed2.val , self.changed1.val
    def iot(self,node):
        if not node:
            return
        self.iot(node.left)
        if node.val <= self.org.val:
            if not self.changed1:
                self.changed1 = self.org
            if self.changed1:
                self.changed2 = node
        self.org = node
        self.iot(node.right)