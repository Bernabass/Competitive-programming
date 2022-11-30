# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level = [ root ]
        res = [(root.val)]
        temp = [ ]
        while level:
            levelX = []
            for i in level:
                if i.left :
                    temp.append(i.left)
                    levelX.append(i.left.val)    
                if i.right:
                    temp.append(i.right)
                    levelX.append(i.right.val)
            if levelX:
                res.append(sum(levelX)/len(levelX))
            level = temp
            temp = [ ]
        return res