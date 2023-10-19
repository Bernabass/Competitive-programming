class parent(defaultdict):
    def __missing__(self, key):
        return key

class UnionFind:
    def __init__(self):
        self.parent = parent()
        self.rank, self.size = defaultdict(int), defaultdict(lambda: 1)

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

        if root_x < root_y:
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def count(self):
        return len({self.find(x) for x in self.parent})

    def group_size(self, x):
        return self.size[self.find(x)]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        N = len(s1)
        uf = UnionFind()
        ans = []
        
        for i in range(N):
            uf.union(s1[i], s2[i])
            
        for char in baseStr:
            ans.append(uf.find(char))
            
        return "".join(ans)