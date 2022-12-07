class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Y = set()
        O = set()
        m, n = len(board),len(board[0])
        neighbours = [[1,0],[-1,0],[0,1],[0,-1]]
        for a in range(m):
            for b in range(n):
                if board[a][b] == 'O':
                    O.add((a,b))
                    for i,j in neighbours:
                        if  0 <= a+i < m and 0 <= b+j < n:
                            pass
                        else:
                            Y.add((a,b))
        def bfs(node,board):
            visited = [node]
            queue = deque([node])
            while queue:
                p = queue.pop()
                board[p[0]][p[1]] = 'y'
                for i , j in [p]:
                    for a , b in neighbours:
                        adj = (i + a, j + b)
                        if 0 <= i+a < m and 0 <= j+b < n and board[adj[0]][adj[1]] == 'O' and adj not in visited:
                            queue.append((i + a , j + b))
                            visited.append((i + a , j + b))
            return board
        while Y:
            temp = Y.pop()
            board = bfs(temp,board)
        for c in range(m):
            for d in range(n):
                if board[c][d] == 'X':
                    for r,s in neighbours:
                        if  0 <= c+r < m and 0 <= d+s < n and board[c+r][d+s] == 'O':
                            board[c+r][d+s] = "X"
        for c in range(m):
            for d in range(n):
                if board[c][d] == 'y':
                    board[c][d] = 'O'