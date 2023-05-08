class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        GRAPH, INDEGREE = defaultdict(list), defaultdict(int)
        order, level = [], []
        
        for child, parent in prerequisites:
            GRAPH[parent].append(child)
            INDEGREE[child] += 1
                           
        for node in range(numCourses):
            if not(INDEGREE[node]):
                level.append(node)
         
        while level:
            next_level = []

            for node in level:
                order.append(node)
                for adj in GRAPH[node]:
                    if INDEGREE[adj]:
                        INDEGREE[adj] -= 1
                        
                        if not (INDEGREE[adj]):
                            next_level.append(adj)
                            
            level = next_level
            
        return order if len(order) == numCourses else []