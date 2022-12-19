class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        m , n = len(board) , len(board[0])
        neighbours = [[1,0],[-1,0],[0,1],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]
        level = [click]
        while level:
            click = level.pop()
            for i , j in  [click]:
                M , adjacent = 0 , []
                for r , c in neighbours:
                    if 0 <= i + r < m and 0 <= j + c < n :
                        if board[i+r][j+c] == "E":
                            adjacent.append([i+r,j+c])
                        if board[i+r][j+c] == "M":
                            M += 1
                if M:
                    board[i][j] = str(M)
                else:
                    board[i][j] = "B"
                    level.extend(adjacent)
        return board