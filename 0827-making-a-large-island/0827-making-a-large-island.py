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
        return len({self.find(x) for x in self.parent})

    def group_size(self, x):
        return self.size[self.find(x)]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        uf = UnionFind()
        max_size = 1
        
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    curr, friend = (i, j), (i, j)
                    for x, y in adj:
                        row, col = i + x, j + y
                        if inbound(row, col) and grid[row][col]:
                            friend = (row, col)
                            uf.union(curr, friend)
                    
                    
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    valids = []
                    for x, y in adj:
                        row, col = i + x, j + y
                        if inbound(row, col) and grid[row][col]:
                            valids.append((row, col))
                            
                    for a, b in valids:
                        curr_size = uf.group_size((a, b)) + 1
                        visited = {uf.find((a, b))}
                        
                        for c, d in valids:
                            curr_parent = uf.find((c, d))
                            if curr_parent not in visited:
                                curr_size += uf.group_size((c, d))
                                visited.add(curr_parent)
                             
                        max_size = max(max_size, curr_size)
                        break
                
                else:
                    max_size = max(max_size, uf.group_size((i, j)))
                                
        return max_size