# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrder(node):
            level = [node]
            if not root:
                return []
            res = [[node.val]]
            while level:
                value = []
                levelX = []
                for i in level:
                    if i.left:
                        levelX.append(i.left)
                        value.append(i.left.val)
                    if i.right:
                        levelX.append(i.right)
                        value.append(i.right.val)
                level = levelX
                if value:
                    res.append(value)
            return res
        return levelOrder(root)