class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        neighbours = [[0,1],[1,0],[-1,0],[0,-1]]
        m, n = len(matrix), len(matrix[0])
        
        def bfs(cell):
            for i, j in [cell]:
                for r, c in neighbours:
                    while 0 <= i+r < m and 0 <= j+c < n:
                        if matrix[i+r][j+c] not in {0,"target"}:
                            matrix[i+r][j+c] = 0
                        i += r
                        j += c
                    i, j = cell[0], cell[1]
                    
        for x in range(m):
            for y in range(n):
                if not matrix[x][y]:
                    matrix[x][y] = "target"

        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "target":
                    bfs([row,col])
        
        for x in range(m):
            for y in range(n):
                if matrix[x][y] == "target":
                    matrix[x][y] = 0