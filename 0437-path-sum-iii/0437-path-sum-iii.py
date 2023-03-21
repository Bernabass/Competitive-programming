# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        pathes = [0]
        
        def go(node, prefix_sum):
            if not node:
                return 
            
            prefix_sum += node.val
            possible_ans = prefix_sum - targetSum
            pathes[0] += freq[possible_ans]
                
            freq[prefix_sum] += 1
            
            go(node.left, prefix_sum)
            go(node.right, prefix_sum)
            freq[prefix_sum] -= 1
            prefix_sum -= node.val
            
            return
        
        go(root, 0)
        return pathes[0]