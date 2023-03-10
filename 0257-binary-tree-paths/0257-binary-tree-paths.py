# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def choose(node_path, val_path, node):
            prev = node_path.copy()
            val_prev = val_path.copy()
            prev.append("->")
            prev.append(node)
            
            
            val_prev.append("->")
            val_prev.append(str(node.val))
            
            next_level.append(prev)
            next_path.append(val_prev)
            
            return
        
        
        level, all_pathes = [[root]], []
        curr_path = [[str(root.val)]]
        curr = deepcopy(level)
        
        while level:
            next_level = []
            next_path = []
            for idx, node_path in enumerate(level):
                val_path = curr_path[idx]
                last_child = node_path[-1]
        
                if not last_child.left and not last_child.right:
                    all_pathes.append(val_path)
                    
                if last_child.left:
                    choose(node_path, val_path, last_child.left)
                    
                if last_child.right:
                    choose(node_path, val_path, last_child.right)
                    
                    
            level = next_level
            curr_path = next_path
            
            
        for idx, path in enumerate(all_pathes):
            all_pathes[idx] = "".join(path)
            
                    
        return all_pathes     