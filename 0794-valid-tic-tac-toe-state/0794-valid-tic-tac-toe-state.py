class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        freq = Counter("".join(board))
        winner = set()
        
        # Checking if the sequence of the turns in the game was valid.
        if (freq["X"] - freq["O"]) not in {0,1}:
            return False
        
        # Checking if there is a winner in a row or in a column.
        for row in range(3):
            if (board[row][0] == board[row][1] == board[row][2]):
                winner.add(board[row][0])
            if (board[0][row] == board[1][row] == board[2][row]):
                winner.add(board[0][row])     
        
        # Checking if there is a winner in one of the main diagonals.
        if (board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2]):
            winner.add(board[1][1])
        
        # There can only be ONE winner with valid TURNS.
        if len(winner) > 1:
            return False
        elif winner == {"X"}:
            return freq["X"] - freq["O"] == 1
        elif winner == {"O"}:
            return freq["X"] - freq["O"] == 0
        return True