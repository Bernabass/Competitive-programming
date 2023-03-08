# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode], isRoot = True) -> int:
        if not root:
            return 0,0,0
        
        left_sum, left_num_nodes, left_count = self.averageOfSubtree(root.left, False)
        right_sum, right_num_nodes, right_count = self.averageOfSubtree(root.right, False)
        
        curr_num_nodes = left_num_nodes + right_num_nodes + 1
        curr_sum = left_sum + right_sum + root.val
        curr_average = (curr_sum // curr_num_nodes)
        count = left_count + right_count
        
        if curr_average == root.val:
            count += 1
            
        if isRoot:
            return count
        
        return curr_sum, curr_num_nodes, count