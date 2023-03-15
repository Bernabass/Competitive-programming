# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            node = root
            
            target = preorder[i]
            left = 0
            while node:
                prev = node
                if node.val > target:
                    node = node.left
                    left = 1
                    
                else:
                    node = node.right
                    left = 0
                    
            if left:
                prev.left = TreeNode(target)

            else:
                prev.right = TreeNode(target)
                          
        return root     