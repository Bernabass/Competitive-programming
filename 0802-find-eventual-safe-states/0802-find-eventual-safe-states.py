class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        GRAPH, INDEGREE = defaultdict(list), defaultdict(int)
        safe_nodes, queue = [], deque()
        
        for node, children in enumerate(graph):
            INDEGREE[node] += len(children)
            for adj in children:
                GRAPH[adj].append(node)
            
            if not children:
                queue.append(node)
                
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            
            for adj in GRAPH[node]:
                if INDEGREE[adj]:
                    INDEGREE[adj] -= 1
                    
                    if not INDEGREE[adj]:
                        queue.append(adj)
                        
        return sorted(safe_nodes)
            
        