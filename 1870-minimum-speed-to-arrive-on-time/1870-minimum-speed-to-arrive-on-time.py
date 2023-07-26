class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        hour = float(hour)
        digits = len(str(hour).split(".")[1])
        n = len(dist)
        
        def check(v):
            t = 0
            for i in range(n - 1):
                q, r = divmod(dist[i], v)
                t += q + (r != 0)
            
            return t + dist[-1] / v
        
        left = 1
        right = 10**7 + 1
        
        while left <= right:
            mid = (left + right) // 2
            time = check(mid)
            
            if time <= hour:
                if mid - 1 and check(mid - 1) <= hour:
                    right = mid - 1
                    
                else:
                    return mid
            
            elif time > hour:
                left = mid + 1
                                        
        return -1