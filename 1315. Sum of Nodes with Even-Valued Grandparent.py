# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        level = [[False,False,root]]
        count = 0
        while level:
            levelX = []
            for i in level:
                if i[0] == True:
                    count += i[2].val
                i.pop(0)
                node = i.pop()
                if node.val % 2 == 0:
                    i.append(True)
                else:
                    i.append(False)
                if node.left:
                    temp = i.copy()
                    temp.append(node.left)
                    levelX.append(temp)
                if node.right:
                    i.append(node.right)
                    levelX.append(i)
            level = levelX
        return count