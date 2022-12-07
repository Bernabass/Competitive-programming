class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        border = set()
        m, n = len(grid),len(grid[0])
        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    for i,j in neighbours:
                        if  0 <= a+i < m and 0 <= b+j < n:
                            pass
                        else:
                            border.add((a,b))
        def bfs(node,grid):
            queue = deque([node])
            while queue:
                p = queue.pop()
                grid[p[0]][p[1]] = 0
                for i , j in [p]:
                    for a , b in neighbours:
                        adj = (i + a, j + b)
                        if 0 <= i+a < m and 0 <= j+b < n and grid[adj[0]][adj[1]] == 1:
                            queue.append((i + a , j + b))
            return grid
        while border:
            temp = border.pop()
            grid = bfs(temp,grid)
        count = 0
        for c in range(m):
            for d in range(n):
                if grid[c][d] == 1:
                    count +=1
        return count