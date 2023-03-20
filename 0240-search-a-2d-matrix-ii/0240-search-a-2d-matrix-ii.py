class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr, target):
            idx = bisect_left(arr, target)
            
            if idx != len(arr) and arr[idx] == target:
                return idx
            
            return -1

        for row in matrix:
            if search(row, target) != -1:
                return True
            
        return False
        
        