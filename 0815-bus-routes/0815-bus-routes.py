class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        GRAPH = defaultdict(list)
        for bus in range(len(routes)):
            curr = -1 - bus
            for route in routes[bus]:
                GRAPH[curr].append(route)
                GRAPH[route].append(curr)
                
        level, seen = [(source, 0)], {source}
        
        
        while level:
            next_level = []
            
            for node, count in level:
                for adj in GRAPH[node]:
                    if adj not in seen:
                        if adj == target:
                            return count

                        next_level.append((adj, count + (adj < 0)))
                        seen.add(adj)
                        
            level = next_level
            
            
        return -1
                    
                    