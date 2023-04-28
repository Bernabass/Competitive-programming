class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        level, seen, steps = [entrance], {tuple(entrance)}, 0
        
        
        def is_inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        while level:
            steps += 1
            next_level = []
            
            for row, col in level:
                for r, c in moves:
                    adj_row, adj_col = row+r, col+c
                    
                    if (adj_row, adj_col) not in seen and is_inbound(adj_row, adj_col) and maze[adj_row][adj_col] == ".":
                        if 0 in (adj_row, adj_col) or adj_row == m-1 or adj_col == n-1:
                            return steps
                        
                        next_level.append((adj_row, adj_col))
                        seen.add((adj_row, adj_col))
                        
            level = next_level
            
        return -1
            
            
            