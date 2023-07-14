class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_square = "1" in matrix[-1]
        for i in range(m):
            max_square = max_square or int(matrix[i][-1])
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j]:
                    E = int(matrix[i][j+1])
                    S = int(matrix[i+1][j])
                    SE = int(matrix[i+1][j+1])

                    matrix[i][j] = min([E, S, SE]) + 1
                    max_square = max(max_square, matrix[i][j])
                
        return max_square**2