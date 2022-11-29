# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs( Q , node ,left ) :
            Q.appendleft(node)
            res=[]
            while Q:
                p = Q.popleft()
                if p is not None:
                    res.append(p.val)
                    if left:
                            Q.appendleft( p.left)
                            Q.appendleft( p.right)
                    else:
                            Q.appendleft( p.right)
                            Q.appendleft( p.left )
                else:
                    res.append(None)
            return res
        Q=deque()
        return bfs(Q,root.left,left=True)==bfs(Q,root.right,left=False)