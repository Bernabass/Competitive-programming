class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n, safe_nodes = len(graph), []
        info = defaultdict(int)
        
        def dfs(node):
            if info[node] == 1:
                return False
            
            elif info[node] == 2:
                return True
            
            info[node] = 2
            
            for adj in graph[node]:
                if dfs(adj):
                    return True
                
            info[node] = 1
            
            return False
        
        for node in range(n):
            if not dfs(node):
                safe_nodes.append(node)
                
        return safe_nodes