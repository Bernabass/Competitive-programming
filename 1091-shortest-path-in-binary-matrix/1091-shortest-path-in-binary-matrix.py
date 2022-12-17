class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        if len(grid[0]) == 1:
            return 1
        neigbours = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        level = [[0,0]]
        memory = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    memory[(i,j)] = 1
        count = 1
        visited = {(0,0)}
        while level:
            levelX = []
            for i , j in level:
                for r , c in neigbours:
                    if 0 <= i+r < n and 0 <= j+c < n and grid[i+r][j+c] == 0 and (i+r,j+c) not in visited:
                        memory[(i+r,j+c)] += count
                        if (i+r,j+c) == (n-1,n-1):
                            return memory[(i+r,j+c)]
                        visited.add((i+r,j+c))
                        levelX.append([i+r,j+c])
            count += 1
            level = levelX
        return -1