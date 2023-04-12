"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        level = [ root ]
        if root is None:
            return 0
        res = [[root.val]]
        temp = [ ]
        count = 0
        while level:
            count += 1
            levelX = []
            for i in level:
                for j in i.children:
                    levelX.append(j)
            level = levelX
        return count