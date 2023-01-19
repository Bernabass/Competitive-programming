class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        odds, evens = set(range(1,10,2)), set(range(0,10,2))
        magic_square = 0
        def isMagicSquare(i,j):
            edges, corners = set([5]), set([0])
            test1 = test2  = 0
            
            for a, b in [[-1,-1],[1,1],[1,-1],[-1,1]]:
                corners.add(grid[i+a][j+b])
                
            for c, d in [[1,0],[0,1],[0,-1],[-1,0]]:
                edges.add(grid[i+c][j+d])
                
            for idx in range(3):
                test1 += grid[i-1][j+idx-1]
                test2 += grid[i+idx-1][j-1]
            
            if test1*test2 == 225 and not((evens-corners)|(odds-edges)):
                return True
            
            return False
            
        for r in range(1,row-1):
            for c in range(1,col-1):
                if grid[r][c] == 5 and isMagicSquare(r,c):
                    magic_square += 1
                    
        return magic_square