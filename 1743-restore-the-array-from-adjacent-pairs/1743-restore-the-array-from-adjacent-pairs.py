class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        GRAPH, seen = defaultdict(list), set()
        original, queue = [], deque()
        
        for node, adj in adjacentPairs:
            GRAPH[node].append(adj)
            GRAPH[adj].append(node)
                        
        for node, adj in GRAPH.items():
            if len(adj) == 1:
                queue.append(node)
                break
                 
        while queue:
            node = queue.popleft()
            original.append(node)
            seen.add(node)
            
            for adj in GRAPH[node]:
                if adj not in seen:
                    queue.append(adj)
                
        return original