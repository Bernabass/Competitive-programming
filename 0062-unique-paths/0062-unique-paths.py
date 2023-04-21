class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def rec(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            if r == m or c == n:
                return 0
            
            return rec(r + 1, c) + rec(r, c + 1)
        return rec(0, 0)