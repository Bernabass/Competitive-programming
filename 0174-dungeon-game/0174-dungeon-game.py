class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        @cache
        def dp(i, j):
            if i == m or j == n:
                return inf
            
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])
            
            right = max(1, dp(i, j + 1) - dungeon[i][j])
            down = max(1, dp(i + 1, j) - dungeon[i][j])
            
            return min(right, down)
        
        return dp(0, 0)