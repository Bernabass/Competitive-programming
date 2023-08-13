class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def valid(target):
            consc = bouquets = 0
            
            for day in bloomDay:
                if day <= target:
                    consc += 1
                    if consc == k:
                        bouquets += 1
                        consc = 0
                        
                else:
                    consc = 0
                    
            return bouquets >= m
        
        left = 0
        right = max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            
            if valid(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return right if valid(right) else -1