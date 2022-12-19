class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        count = 0
        islands1 = set()
        islands2 = set()
        def bfs(grid,node):
            node = [node]
            temp = node
            while node:
                new = []
                for i,j in node:
                    for x,y in neighbours:
                        if 0 <= i+x < m and 0 <= j+y < n and grid[i+x][j+y] == 1:
                            new.append((i+x,j+y))
                            temp.append((i+x,j+y))
                            grid[i+x][j+y] = 0
                node = new
            temp = tuple(temp)
            islands2.add(temp)
            return
        for r in range(m):
            for c in range(n):
                if grid1[r][c] == 1:
                    islands1.add(((r,c)))
                if grid2[r][c] == 1:
                    bfs(grid2,(r,c))
        for i in islands2:
            for j in i:
                if j in islands1:
                    temp = 1
                else:
                    temp = 0
                    break
            if temp:
                count += 1
        return count