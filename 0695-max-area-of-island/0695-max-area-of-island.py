class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        connected = set()
        m, n = len(grid),len(grid[0])
        for a in range(m):
            for b in range(n):
                if grid[a][b] == 1:
                    connected.add((a,b))
        area = 0
        def bfs(node,connected):
            visited = [node]
            queue = deque([node])
            count = 0
            while queue:
                p = queue.pop()
                count += 1
                for i , j in [p]:
                    for a , b in [[1,0],[-1,0],[0,1],[0,-1]]:
                        neighbour = (i + a, j + b)
                        if neighbour in connected and neighbour not in visited:
                            queue.append((i + a , j + b))
                            visited.append((i + a , j + b))
                connected = connected.difference(visited)
            return [count,connected]
        while connected:
            val = connected.pop()
            temp = bfs(val,connected)
            if temp[0] >= area:
                area = temp[0]
            connected = temp[1]
        return area