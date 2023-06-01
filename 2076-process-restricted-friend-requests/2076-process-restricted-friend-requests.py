class my_dict(defaultdict):
    def __missing__(self, key):
        return key
class UnionFind:
    def __init__(self):
        self.parent = my_dict()
        self.rank = defaultdict(int)
        
    def find(self, x):
        original = x
        while self.parent[x] != x:
            x = self.parent[x]

        while self.parent[original] != original:
            original = self.parent[original]
            self.parent[original] = x

        return x
    
    def find2(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x 

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)   
    
    def count(self):
        return len({self.find(x) for x in list(self.parent)})
    
    def setter(self, x, rank):
        self.parent[x] = x
        self.rank[x] = rank

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        uf = UnionFind()
        ans = [True] * len(requests)
        
        for idx, (a, b) in enumerate(requests):
            prev_a, prev_b = uf.find(a), uf.find(b)
            r_a, r_b = uf.rank[a], uf.rank[b]
            uf.union(a, b)
            
            for i, j in restrictions:
                if uf.find2(i) == uf.find2(j):
                    uf.setter(prev_a, r_a)
                    uf.setter(prev_b, r_b)
                    ans[idx] = False
                    break
            
        return ans