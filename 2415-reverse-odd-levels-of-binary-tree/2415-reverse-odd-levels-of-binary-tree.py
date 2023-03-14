# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:    
        info = [[root.val]]  
        curr_level = [root]
        
        while curr_level:
            next_level, curr_info = [], []
                        
            for child in curr_level:
                if child.left:
                    next_level.append(child.left)
                    curr_info.append(child.left.val)
                    
                if child.right:
                    next_level.append(child.right)
                    curr_info.append(child.right.val)
                    
                curr_level = next_level

            if curr_info:
                info.append(curr_info)
                
        new_root = TreeNode(root.val) 
        level = [new_root]
        for idx in range(1, len(info)):
            val = info[idx]
            next_level = []
            
            if idx % 2:
                x = 0
                node = level[x]
                count = len(val)
                i = count - 1
                while i >= 0:
                    node.left = TreeNode(val[i])
                    next_level.append(node.left)
                    i -= 1
                    node.right = TreeNode(val[i])
                    next_level.append(node.right)
                    
                    x += 1
                    i -= 1
                    if x < len(level):
                        node = level[x]
                    
            
            else:
                x = i = 0
                node = level[x]
                count = len(val)
                while i < count:
                    node.left = TreeNode(val[i])
                    next_level.append(node.left)
                    i += 1
                    node.right = TreeNode(val[i])
                    next_level.append(node.right)
                    
                    x += 1
                    i += 1
                    
                    if x < len(level):
                        node = level[x]
                    
            level = next_level
                    
            
        return new_root   