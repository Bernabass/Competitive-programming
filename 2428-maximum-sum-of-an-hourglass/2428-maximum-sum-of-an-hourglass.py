class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        max_sum = 0
        neighbours = [[0,1],[0,2],[1,1],[2,0],[2,1],[2,2]]
        def checker(cell):
            res = 0
            res += grid[cell[0]][cell[1]]
            for i,j in [cell]:
                for r,c in neighbours:
                    res += grid[i+r][j+c]
            return res
        for a in range(row-2):
            for b in range(col-2):
                ans = checker([a,b])
                max_sum = max(max_sum,ans)
        return max_sum
                
                
                
                
                
                
                
                
                
#         for i in range(row):
#             tot=0
#             grid[i].insert(0,0)
#             for j in range(col):
#                 grid[i][j]=tot+grid[i][j]
#                 tot=grid[i][j]
                
#         ans=0
#         print(grid)
#         for i in range(row-2):
#             for j in range(1,col-1):
             
#                 ans=max(ans,grid[i][j+2]-grid[i][j-1]+grid[i+2][j+2]-grid[i+2][j-1]+grid[i+1][j+1]-grid[i+1][j])
                
#         return ans
            
        