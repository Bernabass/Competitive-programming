class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank, self.size = {}, {}
        self.count = n
        
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
        
        self.count -= 1
     
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)   
    
    def count(self):
        return self.count

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        info = {1:[[1, 3, 5], [], [1, 4, 6], []], 2:[[], [2, 3, 4], [], [2, 5, 6]], 3:[[], [], [1, 4, 6], [2, 5, 6]], 4:[[1, 3, 5], [], [], [2, 5, 6]], 5:[[], [2, 3, 4], [1, 4, 6], []], 6:[[1, 3, 5], [2, 3, 4], [], []]}
        
        adj = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        def is_inbound(i, j):
            return 0 <= i < m and 0 <= j < n
        
        level, seen = [(0, 0)], {(0, 0)}
        
        while level:
            next_level = []
            
            for row, col in level:
                if (row, col) == (m-1, n-1):
                    return True
                idx = 0
                for r, c in adj:
                    i, j = row+r, col+c

                    if is_inbound(i, j) and (i, j) not in seen and grid[i][j] in info[grid[row][col]][idx]:
                        next_level.append((i, j))
                        seen.add((i, j))
                        
                    idx += 1   
            level = next_level
                
        return False  