class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        for i in range(n - 2, -1,  -1):
            curr_row = triangle[i]
            for j, num in enumerate(curr_row):
                triangle[i][j] = min(triangle[i+1][j] + num, num + triangle[i+1][j+1])
                
        return min(triangle[0])