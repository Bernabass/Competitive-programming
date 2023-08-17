class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(1, -1), (1, 0), (1, 1)]
        
        def inbound(i, j):
            
            return 0 <= i < m and 0 <= j < n
        
        @cache
        def dp(row1, col1, row2, col2):
            if row1 == m - 1:
                if (row1, col1) == (row2, col2):
                    return grid[row1][col1]
                
                return grid[row1][col1] + grid[row2][col2]
            
            max_cherries = 0
            valid1, valid2 = [], []
            curr1, curr2 = grid[row1][col1], grid[row1][col2]
            for i, j in moves:
                r1, c1 = row1 + i , col1 + j
                r2, c2 = row2 + i , col2 + j
                if inbound(r1, c1):
                    valid1.append((r1, c1))
                
                if inbound(r2, c2):
                    valid2.append((r2, c2))
                    
            for i, j in valid1:
                for x, y in valid2:
                    if (row1, col1) == (row2, col2):
                        grid[row1][col1] = 0
                        max_cherries = max(max_cherries, curr1 + dp(i, j, x, y))
                        grid[row2][col2] = curr1
                        
                    else:
                        grid[row1][col1] = grid[row2][col2] = 0
                        max_cherries = max(max_cherries, curr1 + curr2 + dp(i, j, x, y))
                        grid[row1][col1], grid[row2][col2] = curr1, curr2
                    
            return max_cherries
        
        return dp(0, 0, 0, n - 1)