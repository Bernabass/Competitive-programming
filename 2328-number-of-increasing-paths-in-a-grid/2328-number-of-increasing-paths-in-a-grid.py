class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod, res = 10**9 + 7, 0
        adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n

        @cache
        def dfs(i, j):
            ans = 0
            for r, c in adj:
                x, y = i+r, j+c
                if is_valid(x, y) and grid[x][y] > grid[i][j]:
                    ans += 1 + dfs(x, y)
                    
            return ans
        
        for i in range(m):
            for j in range(n):
                res = (res + (dfs(i, j) % mod)) % mod
        
        return res + m*n