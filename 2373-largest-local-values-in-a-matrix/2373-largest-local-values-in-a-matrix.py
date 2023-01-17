class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        def maker(cell):
            i, j = cell
            mat_max = 0
            if i+2 < n and j+2 < m:
                for row in range(3):
                    for col in range(3):
                        mat_max = max(mat_max,grid[i+row][j+col])
                        
                return mat_max
            
            return 0
         
        idx = 0
        count = 1
        res = []
        for row in range(n-2):
            res.append([])
       
        for row in range(m):
            for col in range(n):
                pos_max = maker([row,col])
                if pos_max:
                    if count > n-2:
                        idx += 1
                        count = 1
                    res[idx].append(pos_max)
                    count += 1
                    
        return res