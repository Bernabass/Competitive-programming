# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:        
        stack, seen = [root], set()
        ans = 0
        
        while stack:
            curr = stack[-1].left
            if curr and curr not in seen:
                stack.append(curr)
            
                
            else:
                popped = stack.pop()
                
                ans += 1
                if ans == k:
                    return popped.val
                
                seen.add(popped)
                if popped.right:
                    stack.append(popped.right)