class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m, n = len(isConnected), len(isConnected[0])
        graph = defaultdict(set)
        provinces = 0
        
        for row in range(m):
            for col in range(n):
                if isConnected[row][col]:
                    graph[row+1].add(col+1)
                    graph[col+1].add(row+1)
                    
        cities = set(graph.keys())

        while cities:
            provinces += 1
            level = [cities.pop()]
            
            while level:
                new_level = []
                for node in level:
                    for adj in graph[node]:
                        if adj in cities:
                            new_level.append(adj)
                            cities.remove(adj)
                            
                level = new_level
                    
        return provinces