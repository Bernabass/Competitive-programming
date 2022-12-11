# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        current = root
        sign = TreeNode(-float('inf'))
        faulty = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                if current.val > sign.val:
                    sign = current
                else:
                    if not faulty:
                        faulty.append(sign)
                        faulty.append(current)
                        sign = current
                    else:
                        faulty[1] = current
                current = current.right
        faulty[0].val, faulty[1].val = faulty[1].val, faulty[0].val