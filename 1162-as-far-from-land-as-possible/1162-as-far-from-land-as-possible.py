class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n , lands, count = len(grid),[],0
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        for a in range(n):
            for b in range(n):
                if grid[a][b] == 1:lands.append((a,b))
        amount = len(lands)
        if not amount or amount == n**2:return -1
        def bfs(node):
            next_land = []
            node = [node]
            for i,j in node:
                for x,y in neighbours:
                    if 0 <= i+x < n and 0 <= j+y < n and grid[i+x][j+y] == 0:
                            grid[i+x][j+y] = 1
                            next_land.append((i+x,j+y))
            return next_land
        while lands:
            temp = []
            for i in lands:
                if amount == n**2:break
                ans = bfs(i)
                amount += len(ans)
                temp.extend(ans)
            lands = []
            if lands ==[] and temp == []:return count
            count += 1
            lands.extend(temp)
        return count