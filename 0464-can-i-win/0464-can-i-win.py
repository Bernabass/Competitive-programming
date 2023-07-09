class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        n = maxChoosableInteger
        total = (n*(n + 1)) // 2
        
        if total < desiredTotal:
            return False
        
        if total == desiredTotal:
            return n % 2
        
        @cache
        def back_track(arr, rem):
            if arr[-1] >= rem:
                return True
            
            for i in range(len(arr)):
                next_candidate = tuple(arr[:i] + arr[i+1:])
                if not(back_track(next_candidate, rem - arr[i])):
                    return True
                
        arr = tuple(range(1, maxChoosableInteger+1))
        
        return back_track(arr, desiredTotal)