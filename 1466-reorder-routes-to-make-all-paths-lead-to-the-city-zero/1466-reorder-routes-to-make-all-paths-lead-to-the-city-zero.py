class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        edges = set(map(tuple, connections))
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

       
        def dfs(node, parent):
            count = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                if (node, neighbor) in edges:
                    edges.remove((node, neighbor))
                    count += 1
           
                count += dfs(neighbor, node)
            return count

       
        removed_count = dfs(0, -1)
        return removed_count
