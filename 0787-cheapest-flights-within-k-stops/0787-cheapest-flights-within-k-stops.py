class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        GRAPH = defaultdict(list)
        
        for node, adj, cost in flights:
            GRAPH[node].append((adj, cost))
          
        @cache
        def dfs(node, stops):
            if node == dst:
                return 0
            
            if stops > k:
                return inf
        
            min_cost = inf
            for adj, cost in GRAPH[node]:
                min_cost = min(min_cost, cost + dfs(adj, stops + 1))
                
            return min_cost
        
        ans = dfs(src, 0)
        
        return -1 if ans == inf else ans