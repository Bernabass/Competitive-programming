class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        count = 0
        def bfs(node):
            node = [node]
            check = True
            while node:
                new = []
                for i,j in node:
                    for x,y in neighbours:
                        if 0 <= i+x < m and 0 <= j+y < n:
                            if grid[i+x][j+y] == 0:
                                new.append((i+x,j+y))
                                grid[i+x][j+y] = 1
                        else:
                            check = False
                node = new
            return check
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    check = bfs((r,c))
                    if check:
                        count += 1
        return count