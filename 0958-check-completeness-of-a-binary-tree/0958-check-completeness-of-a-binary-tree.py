# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([(root, 1)])
        ans = []
        while queue:
            node, position = queue.popleft()
            ans.append(position)
            if node.left:
                queue.append((node.left, 2*position))
            if node.right:
                queue.append((node.right, 2*position+1))
                
        return len(ans) == ans[-1]