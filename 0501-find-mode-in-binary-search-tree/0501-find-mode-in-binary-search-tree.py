# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        freq, seen = defaultdict(int), set()
        
        while stack:
            curr = stack[-1].left
            if curr and curr not in seen:
                stack.append(curr)
            
            else:
                popped = stack.pop()
                freq[popped.val] += 1
                seen.add(popped)
                if popped.right:
                    stack.append(popped.right)
        
        max_rep = max(freq.values())
        ans = []
            
        for node, rep in freq.items():
            if rep == max_rep:
                ans.append(node)
                
        return ans