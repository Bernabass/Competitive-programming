class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0],  matrix[n-1][n-1]

        while low <= high:
            mid = (low + high) // 2
            count = self.countLessOrEqual(matrix, mid)

            if count < k:
                low = mid + 1
                
            else:
                high = mid - 1
                
        return low

    def countLessOrEqual(self, matrix, mid):
        count = row = 0
        col = len(matrix) - 1

        while row < len(matrix) and col >= 0:
            
            if matrix[row][col] > mid:
                col -= 1
                
            else:
                count += col + 1
                row += 1
                
        return count