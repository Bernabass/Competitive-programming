# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def is_in_subtree(root, targets):
            if not root:
                return False
            
            if root in targets:
                return True
            
            root.left = find_LCA(root.left, targets)
            root.right = find_LCA(root.right, targets)
            
            return root.left or root.right 
        
        
        def find_LCA(root, targets):
            if not root:
                return False
            
            if root in targets:
                targets.remove(root)
                flag = is_in_subtree(root, targets)
                
                if flag:
                    return root
                
                return True
            
            root.left = find_LCA(root.left, targets)
            root.right = find_LCA(root.right, targets)
            
            if root.left and root.right:
                return root
            
            return root.left or root.right
                
        return find_LCA(root, {p, q})
                
    
                
                
                
                
                
                
                
                
                