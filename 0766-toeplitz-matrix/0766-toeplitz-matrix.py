class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        diagonals = {}
    
        for m, row in enumerate(matrix):
            for n, element in enumerate(row):
                if m-n not in diagonals:
                    diagonals[m-n] = element
                elif diagonals[m-n] != element:
                    return False
                
        return True      