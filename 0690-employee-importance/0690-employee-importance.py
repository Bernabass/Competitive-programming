"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        GRAPH = defaultdict(list)
        seen = set()
        
        for employee in employees:
            GRAPH[employee.id].append(employee.importance)
            GRAPH[employee.id].append(employee.subordinates)
            
        total_importance = [0]
        
        def dfs(id):
            seen.add(id)
            total_importance[0] += GRAPH[id][0]
            
            for subordinate in GRAPH[id][1]:
                if subordinate not in seen:
                    dfs(subordinate)
                
            return
        
        dfs(id)
        
        return total_importance[0]