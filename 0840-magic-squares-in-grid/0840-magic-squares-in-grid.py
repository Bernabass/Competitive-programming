class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        def checker(i,j):
            odds, evens = set(range(1,10,2)), set(range(0,10,2))
            edges, corners = set([5]), set([0])
            test1 = test2  = 0
            
            for r, c in [[-1,-1],[1,1],[1,-1],[-1,1]]:
                corners.add(grid[i+r][j+c])
                
            for x, y in [[1,0],[0,1],[0,-1],[-1,0]]:
                edges.add(grid[i+x][j+y])
                
            for idx in range(3):
                test1 += grid[i-1][j+idx-1]
                test2 += grid[i+idx-1][j-1]
            
            if test1*test2 == 225 and not((evens-corners)|(odds-edges)):
                return True
            
            return False
            
        for r in range(1,m-1):
            for c in range(1,n-1):
                if grid[r][c] == 5 and checker(r,c):
                    count += 1
                    
        return count