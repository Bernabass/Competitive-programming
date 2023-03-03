class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters.append(float("inf"))
        n = len(heaters)
        optimal_radius = float("-inf")
        
        for home in houses:
            idx1 = idx2 = bisect_left(heaters,home)
            
            if idx1:
                idx2 = idx1 - 1
            
            curr_min = min(abs(home - heaters[idx1]), abs(home - heaters[idx2]))
            optimal_radius = max(optimal_radius, curr_min)
            
        return optimal_radius