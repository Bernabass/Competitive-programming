class parent(defaultdict):
    def __missing__(self, key):
        return key
class UnionFind:
    def __init__(self):
        self.parent = parent()
        self.rank, self.size = defaultdict(int), defaultdict(lambda:1)
        
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
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)   
    
    def count(self):
        return len({self.find(x) for x in list(self.parent)})
    
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        uf = UnionFind()
        adj = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        prev, last_day = set(), 0
        def in_bound(i, j):
            return 1 <= i <= row and 1 <= j <= col
        
        for i in range(1, row+1):
            uf.union((1, 1), (i, 1))
            uf.union((row, col), (i, col))
            
        for i, j in cells:
            last_day += 1
            for r, c in adj:
                x, y = i+r, j+c
                
                if in_bound(x, y) and (x, y) in prev:
                    uf.union((i, j), (x, y))
                    
            prev.add((i, j))
            
            if uf.connected((1, 1), (row, col)):
                return last_day - 1