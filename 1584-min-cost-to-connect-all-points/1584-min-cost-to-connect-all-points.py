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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap, n = [], len(points)
        min_cost = 0
        uf = UnionFind()
        
        for i in range(n):
            for j in range(i+1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                heappush(heap, (dist, (xi, yi), (xj, yj)))
                
        while heap:
            dist, point1, point2 = heappop(heap)
            if not uf.connected(point1, point2):
                min_cost += dist
                uf.union(point1, point2)
                
        return min_cost