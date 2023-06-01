class my_dict(defaultdict):
    def __missing__(self, key):
        return key
class UnionFind:
    def __init__(self):
        self.parent = my_dict()
        self.rank, self.size = defaultdict(int), defaultdict(lambda:1)
        
    def find(self, x):
        original = x
        while self.parent[x] != x:
            x = self.parent[x]

        # while self.parent[original] != original:
        #     original = self.parent[original]
        #     self.parent[original] = x

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
    
    def setter(self, x, par):
        self.parent[x] = par

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        uf = UnionFind()
        ans = [True] * len(requests)
        
        for idx, (a, b) in enumerate(requests):
            prev_a, prev_b = uf.find(a), uf.find(b)
            uf.union(a, b)
            
            for i, j in restrictions:
                if uf.connected(i, j):
                    uf.setter(prev_a, prev_a)
                    uf.setter(prev_b, prev_b)
                    ans[idx] = False
                    break
            
        return ans
