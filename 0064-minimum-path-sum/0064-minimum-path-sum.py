class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @cache
        def back_track(row, col):
            if row == m or col == n:
                return inf
            
            if (row, col) == (m - 1, n - 1):
                return grid[row][col]
            
            
            return grid[row][col] + min(back_track(row+1, col) , back_track(row, col+1))
        
        return back_track(0, 0)