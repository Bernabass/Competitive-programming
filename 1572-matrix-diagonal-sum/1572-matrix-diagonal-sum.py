class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        mid, total = n // 2, 0
        
        for i in range(n):
            total += mat[i][i] + mat[n-1-i][i]
            
        if n % 2:
            total -= mat[mid][mid]
            
        return total