class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target, curr = ((1, 2, 3), (4, 5, 0)), tuple(map(tuple, board))
        adj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def in_bound(i, j):
            return 0 <= i < 2 and 0 <= j < 3
        
        seen, level = {curr}, [curr]
        moves = -1
        
        while level:
            next_level = []
            moves += 1
            
            for curr_board in level:
                if curr_board == target:
                    return moves
                for row in range(2):
                    for col in range(3):
                        if not curr_board[row][col]:
                            for r, c in adj:
                                x, y = row+r , col+c
                                
                                if in_bound(x, y):
                                    temp = list(map(list, curr_board))
                                    temp[row][col], temp[x][y] = temp[x][y], temp[row][col]
                                    temp = tuple(map(tuple, temp))
                                    if temp not in seen:
                                        seen.add(temp)
                                        next_level.append(temp)
                                        
            level = next_level
            
        return -1   