"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        level = [root]
        result = []
        while level:
            levelX = []
            value = []
            for i in level:
                levelX.extend(i.children)
                value.append(i.val)
            level = levelX
            result.append(value)
        return result