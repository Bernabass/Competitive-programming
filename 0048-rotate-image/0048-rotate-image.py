class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        def reverse(arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
        def swap(i, j):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        for row in range(m):
            for col in range(row,n):
                swap(row,col)
          
        for row in matrix:
            reverse(row)