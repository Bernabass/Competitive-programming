class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        @cache
        def back_track(i):
            if i >= n:
                return 0
            
            with_1 = costs[0] + back_track(i + 1)
            
            limit_7, limit_10 = days[i] + 6, days[i] + 29
            
            while i < n and days[i] <= limit_7:
                i += 1
                
            with_7 = costs[1] + back_track(i)
                
            while i < n and days[i] <= limit_10:
                i += 1
                
            with_10 = costs[2] + back_track(i)

            return min(with_1, with_7, with_10)
        
        return back_track(0)