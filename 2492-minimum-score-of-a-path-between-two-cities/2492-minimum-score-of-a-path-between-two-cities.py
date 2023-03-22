class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        def make(v, edges):
            graph = {}
            for i in range(1, v+1):
                graph[i] = []

            for edge in edges:
                parent, child, cost = edge
                graph[parent].append([child, cost])
                graph[child].append([parent, cost])

            return graph

        def bfs(v, edges):
            seen = [False]*(v+1)
            graph = make(v, edges)
            dist = []
            queue = [1]
            ans = float("inf")
            
            while queue:
                node = queue.pop(0)
                if seen[node] == True:
                    continue
                seen[node] = True
                for adj in graph[node]:
                    queue.append(adj[0])
                    dist.append(adj[1])
                        
            return min(dist)
        
        return bfs(n, roads)