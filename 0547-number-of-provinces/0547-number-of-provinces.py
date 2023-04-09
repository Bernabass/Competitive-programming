class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])
        graph = defaultdict(set)
        provinces = [0]
        visited = set()
        
        for row in range(m):
            for col in range(n):
                if isConnected[row][col]:
                    graph[row+1].add(col+1)
                    graph[col+1].add(row+1)
         
        def dfs(node, is_start = True):
            if node in visited:
                return
            
            visited.add(node)
            for adj in graph[node]:
                dfs(adj, False)
                
            provinces[0] += is_start
                
            return
        
        for city in graph.keys():
            dfs(city)
            
        return provinces[0]