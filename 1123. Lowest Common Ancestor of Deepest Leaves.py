# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = [ root ]
        level2 = level.copy()
        while level:
            levelX = []
            for i in level:
                if i.left:
                    levelX.append(i.left)
                if i.right:
                    levelX.append(i.right)
            if not levelX:
                children = level.copy()
            level = levelX
        def bfs(root,children):
            level = [ root ]
            depth = 1
            while level:
                depth += 1 
                if level == children:return depth
                levelX = []
                for i in level:
                    if i.left:
                        levelX.append(i.left)
                    if i.right:
                        levelX.append(i.right)
                level = levelX
            return None
        res = None
        while level2:
            levelX = []
            for i in level2:
                temp = bfs(i,children)
                if temp:
                    res = i
                if i.left:
                    levelX.append(i.left)
                if i.right:
                    levelX.append(i.right)
            level2 = levelX
        return res