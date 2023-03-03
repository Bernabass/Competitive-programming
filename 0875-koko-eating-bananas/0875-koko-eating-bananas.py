class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        
        def hours(pace, total = 0):
            for pile in piles:
                total += math.ceil(pile/pace)
        
        
            return total
        
        
        while left <= right:
            
            mid = (left+right) // 2
            
            if hours(mid) > h:
                left = mid + 1
                
            elif hours(mid) < h:
                right = mid - 1
                
                
                
            else:
                if hours(mid-1) != h:
                    return mid
                
                right = mid - 1
            
            
        return left
            