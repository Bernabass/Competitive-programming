class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def back_track(total, dice):
            if total == target and not dice:
                return 1
            
            if not dice or total > target:
                return 0
            
            ans = 0
            for num in range(1, k + 1):
                ans += back_track(total + num, dice - 1)
            
            
            return ans % (10**9 + 7)
        
        return back_track(0, n) % (10**9 + 7)