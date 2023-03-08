class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, max(time) * totalTrips
        
        while left < right: 
            mid = left + right >> 1
            
            if sum(mid//x for x in time) < totalTrips: 
                left = mid + 1
            else:
                right = mid 
                
        return left 