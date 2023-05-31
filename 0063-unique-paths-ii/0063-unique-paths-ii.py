class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[-1][-1] = 1 - obstacleGrid[-1][-1]
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1 , -1):
                if row == m-1 and col == n-1:
                    continue
                    
                if obstacleGrid[row][col]:
                    obstacleGrid[row][col] = 0
                    
                else:
                    ans = 0
                    if row+1 < m:
                        ans += obstacleGrid[row+1][col]
                        
                    if col+1 < n:
                        ans += obstacleGrid[row][col+1]
                        
                    obstacleGrid[row][col] += ans
                    
        return obstacleGrid[0][0]