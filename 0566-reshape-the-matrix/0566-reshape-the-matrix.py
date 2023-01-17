class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        
        res = [[0]*c for _ in range(r)]
    
        for x, row in enumerate(mat):
            for y, val in enumerate(row):
                count = (x)*n + y
                i, j = count//c, count % c
                res[i][j] += val
                
        return res 