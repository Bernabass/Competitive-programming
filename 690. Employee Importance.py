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
        keys = []
        values = []
        for i in employees:
            keys.append(i.id)
            values.append([i.importance,i.subordinates])
        graph = dict(zip(keys,values))
        queue = deque([id])
        importance = 0
        visited = set()
        while queue:
            p = queue.popleft()
            if p not in visited:
                temp = graph[p]
                visited.add(p)
                importance += temp[0]
                queue.extend(temp[1])
        return importance