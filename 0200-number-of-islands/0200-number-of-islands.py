class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid) - 1
        colums = len(grid[0]) - 1
        ones = set()
        neighbours = [[1,0],[0,1],[-1,0],[0,-1]]
        for r in range(rows + 1):
            for c in range(colums + 1):
                if grid[r][c] == '1':
                    ones.add(((r,c)))
        res = len(ones)
        while ones:
            visited = set()
            node = ones.pop()
            visited.add((node))
            node = [node]
            while node:
                new = []
                for i,j in node:
                    for x,y in neighbours:
                        if (i+x,j+y) in ones and (i+x,j+y) not in visited:
                            new.append((i+x,j+y))
                            visited.add(((i+x,j+y)))
                node = new
            ones -= visited 
            res = res - len(visited) + 1
        return res