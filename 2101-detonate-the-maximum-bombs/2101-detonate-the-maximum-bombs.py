class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        GRAPH = defaultdict(list)
        max_bombs = 1
        
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
                if dist <= r1:
                    GRAPH[i].append(j)

                if dist <= r2:
                    GRAPH[j].append(i)
        
        memo = defaultdict(int)
        
        def dfs(node, seen):
            if node in seen:
                return 0
            
            # if node in memo:
            #     return memo[node]
            
            ans = 1
            seen.add(node)
            for adj in GRAPH[node]:
                ans += dfs(adj, seen)
                
            # memo[node] = ans
                
            return ans
        
        for node in range(len(bombs)):
            if node in GRAPH:
                max_bombs = max(max_bombs, dfs(node, set()))
            
        return max_bombs