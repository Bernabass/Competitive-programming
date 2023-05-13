class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        GRAPH, INDEGREE = defaultdict(list), [0]*n
        level, count = [], 0
        
        for node, adj in edges:
            GRAPH[node].append(adj)
            GRAPH[adj].append(node)
            INDEGREE[node] += 1
            INDEGREE[adj] += 1
            
        for node in range(n):
            if INDEGREE[node] == 1:
                level.append(node)
        
        while level and n - count > 2:
            next_level = []
            
            for node in level:
                INDEGREE[node] -= 1
                count += 1
                for adj in GRAPH[node]:
                    if INDEGREE[adj]:
                        INDEGREE[adj] -= 1

                        if INDEGREE[adj] == 1:
                            next_level.append(adj)
                            
            level = next_level
                      
        return level if n != 1 else [0]