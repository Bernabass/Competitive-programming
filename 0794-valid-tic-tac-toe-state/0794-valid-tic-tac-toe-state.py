class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        freq = Counter("".join(board))
        winner = set()
        if (freq["X"] - freq["O"]) not in {0,1}:
            return False
        
        for row in range(3):
            nth_row, nth_col = set(), set()
            for col in range(3):
                nth_row.add(board[row][col])
                nth_col.add(board[col][row])
           
            if len(nth_row) == 1:
                winner |= nth_row
            if len(nth_col) == 1:
                winner |= nth_col
            
        if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
            winner |= {board[1][1]}
        
        if len(winner) > 1:
            return False
        elif winner == {"X"}:
            return freq["X"] - freq["O"] == 1
        elif winner == {"O"}:
            return freq["X"] - freq["O"] == 0
        return True