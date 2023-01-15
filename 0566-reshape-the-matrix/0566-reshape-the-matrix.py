class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        
        res, count = [], 0
        temp = []
        for row in range(m):
            for col in range(n):
                if count == c :
                    res.append(temp)
                    count = 0
                    temp = []
                count += 1
                temp.append(mat[row][col])
                
        res.append(temp)
        
        return res