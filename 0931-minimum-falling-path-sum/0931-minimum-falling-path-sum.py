class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        mins = {}
        n = len(matrix)
        neighbours = [[1,-1],[1,0],[1,1]]
        path_sum = float('inf')
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                temp = []
                for a,b in neighbours:
                    if 0 <= i+a < n and 0 <= j+b < n:
                        temp.append(mins[(i+a,j+b)])
                if temp:
                    mins[(i,j)] = min(temp) + matrix[i][j]
                else:
                    mins[(i,j)] = matrix[i][j]
        for i in range(n):
            path_sum = min(path_sum,mins[(0,i)])
        return path_sum