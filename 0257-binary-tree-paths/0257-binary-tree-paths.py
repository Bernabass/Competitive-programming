# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def choose(val_path, node):
            val_prev = val_path.copy()
            val_prev.append("->")
            val_prev.append(str(node.val))
            next_path.append(val_prev)
            
            return
        
        level, all_pathes = [root], []
        curr_path = [[str(root.val)]]
        
        while level:
            next_level, next_path = [], []
            for idx, node in enumerate(level):
                val_path = curr_path[idx]
        
                if not node.left and not node.right:
                    all_pathes.append(val_path)
                    
                if node.left:
                    next_level.append(node.left)
                    choose(val_path, node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    choose(val_path, node.right)
                         
            level, curr_path = next_level, next_path
            
        for idx, path in enumerate(all_pathes):
            all_pathes[idx] = "".join(path)
              
        return all_pathes