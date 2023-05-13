class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_GRAPH, row_INDEGREE = defaultdict(list), defaultdict(int)
        col_GRAPH, col_INDEGREE = defaultdict(list), defaultdict(int)
        ans = [[0]*k for _ in range(k)]
        
        for node, adj in rowConditions:
            row_GRAPH[node].append(adj)
            row_INDEGREE[adj] += 1
            
        for node, adj in colConditions:
            col_GRAPH[node].append(adj)
            col_INDEGREE[adj] += 1
            
        def top_sort(graph, indegree):
            queue, order = deque(), {}
            count = 0
            for node in range(1, k+1):
                if not indegree[node]:
                    queue.append(node)
              
            while queue:
                node = queue.popleft()
                order[node] = count
                count += 1
                
                for adj in graph[node]:
                    if indegree[adj]:
                        indegree[adj] -= 1
                        
                        if not indegree[adj]:
                            queue.append(adj)
                            
            return order
        
        row_order = top_sort(row_GRAPH, row_INDEGREE)
        if len(row_order) != k:
            return []
        
        col_order = top_sort(col_GRAPH, col_INDEGREE)
        if len(col_order) != k:
            return []
    
        for node in range(1, k+1):
            row, col = row_order[node], col_order[node]
            ans[row][col] = node
            
        return ans