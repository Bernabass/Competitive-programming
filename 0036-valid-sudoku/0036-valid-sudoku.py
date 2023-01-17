class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [], []
        def sub_box_checker(cell):
            i, j = cell
            seen = set()
            if i+2 < 9 and j+2 < 9:
                for r in range(3):
                    for c in range(3):
                        curr = board[i+r][j+c]
                        if curr.isnumeric():
                            if curr in seen:
                                return False
                            seen.add(curr)
                return True
            return False
        i = 0
        sub_boxes = []
        while i <= 81 and len(sub_boxes) < 9:
            if i % 3 == 0:
                x, y = i // 9, i % 9
                sub_boxes.append(sub_box_checker([x,y]))
            if (i+3) % 9 == 0:
                i += 21
                continue
            i += 3
        
        if not all(sub_boxes):
            return False
        
        for row in range(9):
            new_row, new_col = set(), set()
            for col in range(9):
                row_num = board[row][col]
                col_num = board[col][row]
                
                if row_num.isnumeric():
                    if row_num in new_row:
                        return False
                    new_row.add(board[row][col])
                
                if col_num.isnumeric():
                    if col_num in new_col:
                        return False
                    new_col.add(board[col][row])

        return True