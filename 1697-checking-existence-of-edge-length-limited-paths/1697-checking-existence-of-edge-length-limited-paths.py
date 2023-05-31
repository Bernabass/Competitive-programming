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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n_queries, n_edges = len(queries), len(edgeList)
        uf = UnionFind()
        answer = [False]*n_queries
        
        for i in range(n_queries):
            queries[i].append(i)
         
        edgeList.sort(key = lambda x:x[2])
        queries.sort(key = lambda x:x[2])
        
        idx = 0
        for p, q, limit, org_idx in queries:
            while idx < n_edges and edgeList[idx][2] < limit:
                u, v, dist = edgeList[idx]
                uf.union(u, v)
                idx += 1
            
            answer[org_idx] = uf.connected(p, q)
            
        return answer