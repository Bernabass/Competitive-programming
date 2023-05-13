class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        GRAPH, seen = defaultdict(list), set()
        original = []
        
        for node, adj in adjacentPairs:
            GRAPH[node].append(adj)
            GRAPH[adj].append(node)
            
        def dfs(node, parent):
            seen.add(node)
            original.append(node)

            for adj in GRAPH[node]:
                if adj != parent and adj not in seen:
                    dfs(adj, node)
            
            
        for node, adj in GRAPH.items():
            if len(adj) == 1:
                dfs(node, "front")
                break
                
        return original