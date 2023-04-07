class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        perimeter = 0
        
        def check(row, col):
            count = 0
            for r, c in directions:
                new_row, new_col = row+r, col+c
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col]:
                        count += 1
                        
            return count
                
        
        for row in range(m):
            for col in range(n):
                
                if grid[row][col]:
                    perimeter += 4 - check(row, col)
                    
        return perimeter
                    