class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [], []
        def sub_box_checker(cell):
            i, j = cell
            seen = set()
            for r in range(3):
                for c in range(3):
                    curr = board[i+r][j+c]
                    if curr.isnumeric():
                        if curr in seen:
                            return False
                        seen.add(curr)
            return True
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not sub_box_checker([i,j]):
                    return False

        for row in range(9):
            new_row, new_col = set(), set()
            for col in range(9):
                row_num, col_num = board[row][col], board[col][row]
                
                if row_num.isnumeric():
                    if row_num in new_row:
                        return False
                    new_row.add(board[row][col])
                
                if col_num.isnumeric():
                    if col_num in new_col:
                        return False
                    new_col.add(board[col][row])

        return True