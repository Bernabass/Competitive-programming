class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        diagonal = defaultdict(set)
        
        for row in range(m):
            for col in range(n):
                diagonal[row-col].add(matrix[row][col])
                
        for val in diagonal.values():
            if len(val) != 1:
                return False
        
        return True