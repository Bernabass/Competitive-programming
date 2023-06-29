class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        keys, locks = "abcdef", "ABCEDEF"
        adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        total_keys, queue = 0, deque([])
        
        def in_bound(i, j):
            return 0 <= i < m and 0 <= j < n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    queue.append((i, j, (), 0))
                    
                elif grid[i][j] in keys:
                    total_keys += 1

        seen = set()

        while queue:
            i, j, curr_key, moves = queue.popleft()
            curr = grid[i][j]

            if curr in locks and curr.lower() not in curr_key or curr == "#":
                continue

            if curr in keys:
                if curr not in curr_key:
                    curr_key += (curr,)
                if len(curr_key) == total_keys:
                    return moves

            for r, c in adj:
                x, y = i+r, j+ c
                if  in_bound(x, y) and (x, y, curr_key) not in seen:
                    seen.add((x, y, curr_key))
                    queue.append((x, y, curr_key, moves+1))

        return -1