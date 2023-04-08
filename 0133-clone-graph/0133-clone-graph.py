"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':        
        if not node:
            return None

        cloned_nodes = {}
        visited = set()
        queue = collections.deque([node])

        while queue:
            curr_node = queue.popleft()
            if curr_node in visited:
                continue

            visited.add(curr_node)

            if curr_node not in cloned_nodes:
                cloned_nodes[curr_node] = Node(curr_node.val)

            for neighbor in curr_node.neighbors:
                if neighbor not in cloned_nodes:
                    cloned_nodes[neighbor] = Node(neighbor.val)

                cloned_nodes[curr_node].neighbors.append(cloned_nodes[neighbor])
                queue.append(neighbor)

        return cloned_nodes[node]
                