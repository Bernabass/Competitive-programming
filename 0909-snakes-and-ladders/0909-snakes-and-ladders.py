class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def coordinate(val):        
            row = n - ((val - 1) // n) - 1
            col = (val - 1) % n
            
            if not((n- row) % 2):
                col = n - col - 1

            return row, col
           
        level, seen, depth = [1], {0}, 0
            
        while level:
            depth += 1
            next_level = []

            for curr in level:
                for adj in range(curr+1, min(curr+6, n**2)+1):
                    if adj not in seen:
                        if adj == n**2:
                            return depth

                        i, j = coordinate(adj)
                        rep = board[i][j]
                        if rep == -1:
                            next_level.append(adj)

                        else:
                            if rep == n**2:
                                return depth
                            next_level.append(rep)
                            
                        seen.add(adj)

            level = next_level

        return -1