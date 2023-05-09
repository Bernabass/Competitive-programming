class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        GRAPH = defaultdict(list)
        answer = [set() for _ in range(n)]
        
        for src, dest in edges:
            GRAPH[dest].append(src)
            
            
        def bfs(node, seen):
            level = [node]
            seen.add(node)
            org = node
            
            while level:
                next_level = []
                
                for node in level:
                    for adj in GRAPH[node]:
                        if adj not in seen:
                            answer[org].add(adj)
                            seen.add(adj)

                            if answer[adj]:
                                answer[org] |= answer[adj]

                            else:
                                next_level.append(adj)

                level = next_level
        
        for node in range(n):
            bfs(node, set())
            
        return [sorted(list(curr)) for curr in answer]