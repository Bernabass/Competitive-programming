class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        adj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result, seen, level = [[0]*n for _ in range(m)], set(), 0
        zeros = [(row, col) for row in range(m) for col in range(n) if not mat[row][col]]
      
        def is_inbound(row, col):
            return 0 <= row < m and 0 <= col < n
                    
        while zeros:
            next_level = []
            level += 1
            
            for row, col in zeros:
                for r, c in adj:
                    adj_row, adj_col = row+r, col+c
                    if (adj_row, adj_col) not in seen and is_inbound(adj_row, adj_col) and mat[adj_row][adj_col]:
                        result[adj_row][adj_col] += level
                        next_level.append((adj_row, adj_col))
                        seen.add((adj_row, adj_col))
                        
            zeros = next_level
            
        return result 