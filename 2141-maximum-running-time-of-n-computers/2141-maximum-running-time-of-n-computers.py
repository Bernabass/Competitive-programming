class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        def valid(minute):
            total = 0
            
            for val in batteries:
                total += min(minute, val)
                
            return total >= n * minute
        
        left = 1
        right = sum(batteries)
        
        while left <= right:
            mid = (left + right) // 2
            
            if valid(mid):
                if not valid(mid + 1):
                    return mid
                
                left = mid + 1
                
            else:
                right = mid - 1
                
        return left