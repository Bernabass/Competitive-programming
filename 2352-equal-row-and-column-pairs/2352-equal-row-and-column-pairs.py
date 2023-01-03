class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows, columns = defaultdict(int), []
        count = 0
        for i in range(n):
            temp1, temp2 = [], []
            for j in range(n):
                temp1.append(grid[i][j])
                temp2.append(grid[j][i])
            rows[tuple(temp1)] += 1
            columns.append(tuple(temp2))
        
        for k in range(n):
            if columns[k] in rows:
                count += rows[columns[k]]
        
        return count
