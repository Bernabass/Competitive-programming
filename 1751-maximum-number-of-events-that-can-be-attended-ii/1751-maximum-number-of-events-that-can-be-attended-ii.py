class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort()

        @cache
        def back_track(idx, k):
            if k == 0 or idx >= n :
                return 0
            
            j = idx
            while j < n and events[j][0] <= events[idx][1]:
                j += 1
                
            curr1 = events[idx][2] + back_track(j, k - 1)

            curr2 = back_track(idx + 1 ,k)

            return max(curr1, curr2)
    
        return back_track(0, k)