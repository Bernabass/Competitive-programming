# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level, res = [root], [root.val]
        
        while level:
            levelX, curr_sum = [], 0
            for i in level:
                if i.left :
                    curr_sum += i.left.val
                    levelX.append(i.left)    
                if i.right:
                    curr_sum += i.right.val
                    levelX.append(i.right)
                    
            if levelX:
                res.append(curr_sum/len(levelX))
                
            level = levelX
            
        return res