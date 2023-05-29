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
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        uf, n = UnionFind(), len(source)
        info = defaultdict(lambda: defaultdict(int))
        hamming_dist = 0
        
        for a, b in allowedSwaps:
            uf.union(a, b)
            
        for i in range(n):
            rep = uf.find(i)
            info[rep][source[i]] += 1
        
        for j in range(n):
            rep = uf.find(j)
            if info[rep][target[j]] > 0:
                info[rep][target[j]] -= 1

            else:
                hamming_dist += 1
                    
        return hamming_dist
            