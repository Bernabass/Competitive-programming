# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def make_tree(arr):
            if not arr:
                return [None]
            
            ans = []
            for idx, val in enumerate(arr):
                left, right = make_tree(arr[:idx]), make_tree(arr[idx+1:])
                
                for left_node in left:
                    for right_node in right:
                        curr_node = TreeNode(val)
                        curr_node.left = left_node
                        curr_node.right = right_node
                        ans.append(curr_node)
                        
            return ans
                        
        return make_tree(list(range(1,n+1)))
                    