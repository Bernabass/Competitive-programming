class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = tuple(sum(mat, []))
        target = tuple([0] * (m * n))
        
        if start == target:
            return 0
        
        seen = set()
        seen.add(start)
        
        def flip(matrix, r, c):
            for i, j in [(r, c), (r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= i < m and 0 <= j < n:
                    matrix[i * n + j] ^= 1
            return matrix
        
        queue = deque([(start, 0)])
        
        while queue:
            curr, depth = queue.popleft()
            for i in range(m):
                for j in range(n):
                    next_state = flip(list(curr), i, j)
                    if tuple(next_state) == target:
                        return depth + 1
                    if tuple(next_state) not in seen:
                        seen.add(tuple(next_state))
                        queue.append((tuple(next_state), depth + 1))
        
        return -1