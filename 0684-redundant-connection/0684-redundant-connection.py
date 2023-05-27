class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank, self.size = {}, {}
        self.count = n
        
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            self.size[x] = 1

    def find(self, x):
        original = x
        while self.parent[x] != x:
            x = self.parent[x]

        while self.parent[original] != original:
            original = self.parent[original]
            self.parent[original] = x

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            self.rank[root_x] += 1
        
        self.count -= 1
     
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)   
    
    def count(self):
        return self.count

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        groups = UnionFind(len(edges))
        
        for i in range(1, len(edges)+1):
            groups.add(i)
            
        for a, b in edges:
            if groups.is_connected(a, b):
                return [a, b]
            
            else:
                groups.union(a, b)