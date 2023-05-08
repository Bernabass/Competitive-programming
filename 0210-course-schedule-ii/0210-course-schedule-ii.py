class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        GRAPH = defaultdict(list)
        order = []
        black, grey = set(), set()
        
        for child, parent in prerequisites:
            GRAPH[parent].append(child)

        def dfs(node): 
            grey.add(node)
            cycle = False
            
            for adj in GRAPH[node]:
                if adj in grey:
                    return True
                    
                elif adj not in black:
                    cycle |= dfs(adj)
                          
            grey.remove(node)       
            black.add(node)
            order.append(node)
            
            return cycle
        
        for node in range(numCourses):
            if node not in black:
                cycle = dfs(node)
                if cycle:
                    return []
                
        return reversed(order)
                    
                    
                    