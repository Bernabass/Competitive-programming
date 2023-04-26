class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        spoiled, normal = set(), set()
        m, n = len(grid), len(grid[0])
        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        count = 0
        
        for row in range(m):
            for column in range(n):
                if grid[row][column] == 1:
                    normal.add((row,column))
                elif grid[row][column] == 2:
                    spoiled.add((row,column))
                    
        while normal:
            count += 1
            temp = set()
            for i, j in spoiled:
                for x, y in neighbours:
                    if (i+x, j+y) in normal:
                        temp.add((i+x,j+y))
            if not temp:
                return -1
            
            normal -= temp
            spoiled = temp
            
        return count