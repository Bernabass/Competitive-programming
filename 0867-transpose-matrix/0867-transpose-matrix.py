class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m , n  = len(matrix) , len(matrix[0])
        res = []
        for j in range(n):
            temp = []
            for i in range(m):
                temp.append(matrix[i][j])
            res.append(temp)
        return res