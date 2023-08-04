class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        self.ans = 0
        GRAPH = defaultdict(dict)
        for u, v, time in edges:
            GRAPH[u][v] = time
            GRAPH[v][u] = time
        
        def dfs(node, seen, score, cost):
            if not node:
                self.ans = max(self.ans, score)
            
            for adj, time in GRAPH[node].items():
                if time <= cost:
                    new_seen = seen | {adj}
                    
                    if adj not in seen:
                        new_score = score + values[adj]
                        
                    else:
                        new_score = score
                        
                    new_cost = cost - time
                    
                    dfs(adj, new_seen, new_score, new_cost)

        
        dfs(0, {0}, values[0], maxTime)
        
        return self.ans