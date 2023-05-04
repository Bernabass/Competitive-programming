# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        GRAPH = defaultdict(list)
        def dfs(node):
            if not node:
                return 
            
            left = dfs(node.left)

            if left:
                GRAPH[node.val].append(left)
                GRAPH[left].append(node.val)
                
            right = dfs(node.right)
            
            if right:
                GRAPH[node.val].append(right)
                GRAPH[right].append(node.val)
            
            return node.val
        
        dfs(root)
        
        level, seen = [target.val], {target.val}
        distance = -1
        
        while level:
            distance += 1
            if distance == k:
                return level
            
            next_level = []
            
            for node in level:
                for adj in GRAPH[node]:
                    if adj not in seen:
                        next_level.append(adj)
                        seen.add(adj)
                

            
            level = next_level
            
        return []