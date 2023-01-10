class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = deque([[0,1],[1,0],[0,-1],[-1,0]])
        ans, cell = [], [0,0]
        for _ in range(m*n):
            i, j = cell[0], cell[1]
            ans.append(matrix[i][j])
            matrix[i][j], flag = 101, False
            for r, c in directions:
                if 0 <= i+r < m and 0 <= j+c < n and matrix[i+r][j+c] != 101:
                    cell = [i+r,j+c]
                    break
                flag = True
            if flag:
                last = directions.popleft()
                directions.append(last)
                      
        return ans