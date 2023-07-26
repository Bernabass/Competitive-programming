class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        adj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        empties = self.count = 0
        seen = set()
        
        for i in range(m):
            for j in range(n):
                empties += grid[i][j] in {0, 2}
                if grid[i][j] == 1:
                    row, col = i, j
                
        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n
                
        
        def back_track(i, j):
            if grid[i][j] == 2:
                self.count += len(seen) == empties
                return
                
            if len(seen) == empties:
                return
            
            for r, c in adj:
                row, col = i + r, j + c
                if (row, col) not in seen and inbound(row, col) and grid[row][col] in {0, 2}:
                    seen.add((row, col))
                    back_track(row, col)
                    seen.remove((row, col))

        back_track(row, col)
        
        return self.count