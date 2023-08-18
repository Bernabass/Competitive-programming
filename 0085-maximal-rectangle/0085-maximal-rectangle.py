class MyDict(defaultdict):
    def __missing__(self, key):
        return [(0, 0), (0, 0), (0, 0)]

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = defaultdict(int)
        max_area = 0
        def NextZero(row, col):
            stack = [col]
            dp[(row, col)] = n
            
            for idx in range(col + 1, n):
                if matrix[row][idx] == "0": 
                    while stack:
                        dp[(row, stack.pop())] = idx
                        
                else:
                    stack.append(idx)
                    
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    NextZero(row, col)
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    width, length = n, row
                    
                    while length < m and matrix[length][col] == "1":
                        width = min(width, dp[(length, col)] - col)
                        max_area = max(max_area, (length - row + 1) * width)
                        length += 1
                        
        return max_area
                    