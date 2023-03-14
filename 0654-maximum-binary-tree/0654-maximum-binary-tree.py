# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        
        def make_tree(node, arr):
            if not arr:
                node = None
                return node
                
            curr_max = max(arr)
            left = arr[:arr.index(curr_max)]
            right = arr[arr.index(curr_max)+1:]
            
            node.val = curr_max
            node.left = make_tree(TreeNode(), left)
            node.right = make_tree(TreeNode(), right)
            
            return node
        
        make_tree(root, nums)
        
        return root