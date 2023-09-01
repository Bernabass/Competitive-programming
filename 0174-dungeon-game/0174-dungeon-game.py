class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        @cache
        def dp(i, j):
            if i == m or j == n:
                return float("inf")
            
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            
            right = dp(i, j + 1)
            down = dp(i + 1, j)
            
            return max(1, min(right, down) - dungeon[i][j])
        
        return dp(0, 0)