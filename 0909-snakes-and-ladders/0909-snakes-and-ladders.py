class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, seen = len(board), set()
        
        def coordinate(val):        
            row = (val - 1) // n
            row = n - row - 1

            col = (val - 1) % n
            if (n- row) % 2 == 0:
                col = n - col - 1

            return row, col
        
        def roll_die(curr):
            start, end = [curr+1, min(curr+6, n**2)]

            return [value for value in range(start, end+1)]
            
        def bfs(node):
            level, depth = [node], 0
            seen.add(node)
            
            while level:
                depth += 1
                next_level = []
                
                for value in level:
                    destination = roll_die(value)
                    
                    for adj in destination:
                        if adj not in seen:
                            if adj == n**2:
                                return depth
                            
                            seen.add(adj)
                            
                            i, j = coordinate(adj)
                            rep = board[i][j]
                            if rep == -1:
                                next_level.append(adj)
                                
                            else:
                                if rep == n**2:
                                    return depth
                                next_level.append(rep)
                                    
                level = next_level
                
            return -1
                
        return bfs(1)