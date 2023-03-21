class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        
        def attacked_squares(i, j, place):
            neighbours = [[1,-1],[0,1],[1,0],[1,1]]
            if place:
                board[i][j] += 1
            else:
                board[i][j] -= 1
            
            for r, c in neighbours:
                row, col = i, j
                while 0 <= row+r < n and 0 <= col+c < n:
                    row, col = row+r, col+c 
                    if place:
                        board[row][col] += 1
                        
                    else:
                        board[row][col] -= 1
                        
        def backtrack(row = 0, count = 0):
            for col in range(n):
                if not board[row][col]:
                    attacked_squares(row, col, 1)
                                     
                    if row + 1 == n:
                        count += 1
                    else:

                        count = backtrack(row + 1, count)
                    attacked_squares(row, col, 0)
                    
            return count
        
        return backtrack()