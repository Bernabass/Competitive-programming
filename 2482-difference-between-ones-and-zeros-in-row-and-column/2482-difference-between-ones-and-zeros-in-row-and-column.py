class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m , n = len(grid) , len(grid[0])
        onesRow = defaultdict(int)
        onesCol = defaultdict(int)
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    onesRow[row] += 1
                    onesCol[col] += 1
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (onesRow[i] + onesCol[j]) - (m + n)
                
        return grid