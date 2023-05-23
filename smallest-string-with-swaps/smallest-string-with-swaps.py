class UnionFind:
    def __init__(self, length):
        self.parent = {}
        self.rank = {}
        self.size = {}
        self.length = length
        
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
        
        self.length -= 1
        
    def length(self):
        return self.length

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        info, n = defaultdict(list), len(s)
        groups, ans = UnionFind(n), []
        
        for i in range(n):
            groups.add(i)
        
        for idx1, idx2 in pairs:
            groups.union(idx1, idx2)
            
        for j in range(n):
            rep = groups.find(j)
            heappush(info[rep], s[j])
            
        for k in range(n):
            rep = groups.find(k)
            ans.append(heappop(info[rep]))
            
        return "".join(ans)