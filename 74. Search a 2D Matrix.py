class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows=len(matrix)
        columns=len(matrix[0])
        left=0
        right=(rows*columns)-1
        while left<=right:
            mid=(left+right)//2
            mn=matrix[mid//columns][mid%columns]
            if target<mn:
                right=mid-1
            elif target>mn:
                left=mid+1
            else:
                return True
        return False
        