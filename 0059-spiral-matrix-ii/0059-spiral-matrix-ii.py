class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = deque([[0, 1],[1, 0],[0, -1],[-1 ,0]])
        ans = [[0]*n for _ in range(n)]
        i = j = count = 0
        
        for count in range(1, n*n + 1):
            ans[i][j] += count
            flag = False
            for r, c in directions:
                if 0 <= i + r < n and 0 <= j + c < n and not ans[i + r][j + c]:
                    i, j = i + r, j + c
                    break
                else:
                    flag = True
            if flag:
                directions.rotate(-1)
                      
        return ans