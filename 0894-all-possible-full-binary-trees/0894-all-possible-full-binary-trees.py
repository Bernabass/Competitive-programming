# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if not (n % 2):
            return []
        
        self.org = n
        def back_track(n):
            if n == -1:
                return [(0, None)]
                
            sub_tree = back_track(n - 2)
            res = []
            
            if self.org != n:
                res = sub_tree.copy()
            
            for LC, left_tree in sub_tree:
                for RC, right_tree in sub_tree:
                    CC = LC + RC + 1
                    if CC == n:
                        if self.org == n:
                            res.append(TreeNode(0, left_tree, right_tree))
                              
                        else:
                            res.append((CC, TreeNode(0, left_tree, right_tree)))
                
            return res
        
        return back_track(n)