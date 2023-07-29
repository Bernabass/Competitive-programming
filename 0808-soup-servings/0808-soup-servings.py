class Solution:
    def soupServings(self, n: int) -> float:
        operations = [[-100, 0], [-75, -25], [-50, -50], [-25, -75]]
        
        if n >= 5000:
            return 1
        
        @cache
        def back_track(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            
            if a <= 0:
                return 1
            
            if b <= 0:
                return 0
            
            count = 0
            for i, j in operations:
                count += back_track(a + i, b + j)
                
            return 0.25 * count
        
        return back_track(n, n)