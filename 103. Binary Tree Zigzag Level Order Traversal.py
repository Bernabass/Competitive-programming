# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = [ root ]
        if root is None:
            return []
        res = [[root.val]]
        temp = [ ]
        count = 1
        while level:
            levelX = []
            for i in level:
                if i.left :
                    temp.append(i.left)
                    levelX.append(i.left.val)    
                if i.right:
                    temp.append(i.right)
                    levelX.append(i.right.val)
            if count %2 != 0:
                levelX.reverse()
            if levelX !=[]:
                res.append(levelX)
            level = temp
            temp = [ ]
            count+=1
        return res