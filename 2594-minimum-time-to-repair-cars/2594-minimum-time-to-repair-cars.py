class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        N = len(ranks)
        def CanRepair(time):
            total = 0
            for curr_rank in ranks:
                total += int((time // curr_rank)**0.5)
                
            return total >= cars

        
        left = 0
        right = max(ranks)*(cars **2) * N
        
        while left < right:
            mid = (left + right) // 2
            
            if CanRepair(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return right