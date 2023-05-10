class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n, safe_nodes = len(graph), []
        info = ["unvisited"] * n
        
        def dfs(node):
            if info[node] == "safe":
                return False
            
            elif info[node] == "unsafe":
                return True
            
            info[node] = "unsafe"
            
            for adj in graph[node]:
                if dfs(adj):
                    return True
                
            info[node] = "safe"
            
            return False
        
        for node in range(n):
            if not dfs(node):
                safe_nodes.append(node)
                
        return safe_nodes      