class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        seen, edges = set(), set()

        def picker(n):
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        
                        return (i, j)
                    
        def is_inbound(row, col):
            
            return 0 <= row < n and 0 <= col < n
                
        def bfs(cells, connect):
            if connect:
                for node in cells:
                    seen.add(node)
                    
            level, limit = 0, True
            
            while cells and limit:
                level += 1
                next_cells = []
                
                for row, col in cells:
                    for r, c in neighbours:
                        i, j = row+r, col+c

                        if is_inbound(i, j):
                            if connect:
                                if (i, j) not in seen:
                                    if grid[i][j] == 0:
                                        next_cells.append((i, j))
                                        seen.add((i, j))

                                    elif grid[i][j] == 1:
                                        limit = False
                                        break

                            else:
                                if grid[i][j] == 1:
                                    grid[i][j] = 2
                                    next_cells.append((i, j))

                                elif grid[i][j] == 0:
                                    edges.add((row, col))   
                
                cells = next_cells
                                
            return level - 1
        
        bfs([picker(n)], 0)
        
        return bfs(edges, 1)                    