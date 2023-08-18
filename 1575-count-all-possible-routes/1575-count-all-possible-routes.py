class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(start, fuel):
            another = 0
            if fuel < 0:
                return another
            
            if start == finish:
                another += 1
        
            count = 0
            for i in range(len(locations)):
                if i != start:
                    count += dp(i, fuel - abs(locations[i] - locations[start]))
                    
            return (count + another) % MOD
                                
        return dp(start, fuel)