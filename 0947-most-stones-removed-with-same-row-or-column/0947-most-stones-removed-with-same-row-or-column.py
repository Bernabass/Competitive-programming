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
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        un = UnionFind(n)
        
        for st in stones:
            if tuple(st) not in un.parent:
                un.add(tuple(st))
            
            for prev in un.parent:
                if prev[0] == st[0] or prev[1] == st[1]:
                    un.union(tuple(st), tuple(prev))
        
        return n - un.count
        
