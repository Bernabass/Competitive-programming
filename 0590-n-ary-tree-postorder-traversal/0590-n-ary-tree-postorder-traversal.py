"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        seen = set()
        level = [root]
        result = []
        while level:
            p = level.pop()
            if p.children == [] or p in seen:
                result.append(p.val)
            else:
                level.append(p)
                seen.add(p)
                level.extend(p.children[::-1])
        return result