# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def levelOrder(node):
            level = [node]
            res = [node]
            while level:
                levelX = []
                for i in level:
                    if i.right:
                        levelX.append(i.right)
                    if i.left:
                        levelX.append(i.left)
                level = levelX
                res.extend(level)
            return res
        def postOrder(node):
            res = levelOrder(node)
            res.reverse()
            return res
        nodes = postOrder(root)
        best = {}
        optimal = -float('inf')
        for i in nodes:
            temp = -float('inf')
            if not i.left and not i.right:
                best[i] = i.val
                continue
            if i.left:
                temp = max(temp,best[i.left])
            if i.right:
                temp = max(temp,best[i.right])
            ans = max(temp + i.val,i.val)
            best[i] = ans
        for i in best:
            node_max = i.val
            if not i.left and not i.right:
                optimal = max(optimal, node_max)
                continue
            if i.left:
                node_max += best[i.left]
            if i.right:
                node_max += best[i.right]
            optimal = max(optimal,i.val)
            optimal = max(optimal, best[i])
            optimal = max(optimal, node_max)
        return optimal