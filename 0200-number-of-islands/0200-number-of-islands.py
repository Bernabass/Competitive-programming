class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        count = 0
        def bfs(node):
            node = [node]
            while node:
                new = []
                for i,j in node:
                    for x,y in neighbours:
                        if 0 <= i+x < m and 0 <= j+y < n and grid[i+x][j+y] == '1':
                            new.append((i+x,j+y))
                            grid[i+x][j+y] = '0'
                node = new
            return 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    bfs((r,c))
                    count += 1
        return count