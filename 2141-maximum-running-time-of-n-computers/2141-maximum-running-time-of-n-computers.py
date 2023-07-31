class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def valid(minute):
            total = 0
            
            for val in batteries:
                total += min(minute, val)
                
            return total >= n * minute
        
        left = 0
        right = sum(batteries) // n + 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if valid(mid):
                left = mid + 1
                
            else:
                right = mid - 1
                
        return right