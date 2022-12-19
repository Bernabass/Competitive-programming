class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        if len(grid[0]) == 1:
            return 1
        adj = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
        def bfs(node):
            result = set()
            level = [node]
            visited = {(node[0],node[1])}
            for i , j in level:
                for r , c in adj:
                    if 0 <= i+r < n and 0 <= j+c < n and grid[i+r][j+c] == 0 and (i+r,j+c) not in visited:
                        visited.add((i+r,j+c))
                        result.add((i+r,j+c))
            return result
        front = {(0,0)}
        back = {(n-1,n-1)}
        count_f = 1
        count_b = 1
        seen = set()
        flag = False
        while not flag:
            flag = True
            org = front.copy()
            count_org = count_f
            for x,y in front:
                if (x,y) not in seen:
                    flag = False
                    seen.add((x,y))
                    ans = bfs((x,y))
                    front = front.union(ans)
            count_f += 1
            if front & back:
                return count_f + count_b - 1
            for a,b in back:
                if (a,b) not in seen:
                    flag = False
                    seen.add((a,b))
                    ans = bfs((a,b))
                    back = back.union(ans)
            count_b += 1
            if org & back:
                return count_org + count_b - 1
            if front & back:
                return count_f + count_b - 1
        return -1