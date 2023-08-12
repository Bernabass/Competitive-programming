class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = sum(matrix[-1])
        
        for row in range(m - 1):
            count += matrix[row][-1]
                
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                
                if matrix[i][j]:
                    right = matrix[i][j + 1]
                    bottom_right = matrix[i + 1][j + 1]
                    bottom = matrix[i + 1][j]
                    
                    matrix[i][j] += min(right, bottom_right, bottom)
                    
                count += matrix[i][j]
                
        return count