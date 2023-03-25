class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def bfs(adj, u, lookup):
            level = [u]
            lookup[u] = 1
            result = 1
            while level:
                new_level = []
                for u in level:
                    for v in adj[u]:
                        if lookup[v]:
                            continue
                        lookup[v] = 1
                        result += 1
                        new_level.append(v)
                level = new_level
            return result
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [0]*n
        result = 0
        for u in range(n):
            if lookup[u]:
                continue
            count = bfs(adj, u, lookup)
            result += count*(n-count)
            n -= count
            
        return result

