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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        names = defaultdict(list)
        merged = defaultdict(set)
        ans = []
        uf = UnionFind()
        num = 0
        
        for account in accounts:
            name = account[0] + ":" + str(num)
            num += 1
            
            for i in range(1, len(account)):
                curr_email = account[i]
                uf.union(curr_email, account[1])
                names[curr_email] = name
                   
        for account in accounts:            
            for i in range(1, len(account)):
                curr_email = account[i]
                merged[names[uf.find(curr_email)]].add(curr_email)
                
        for key, val in merged.items():
            name, _ = key.split(":")
            ans.append([name] + sorted(val))
        
        return ans