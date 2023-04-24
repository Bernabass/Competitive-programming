class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        @cache
        def back_track(idx):
            if not idx:
                return 1

            ans = 0
            for i in range(idx-1, -1, -1):
                if not(int(s[i])): 
                    continue
                    
                elif int(s[i:idx]) <= k:
                    ans += back_track(i) % (10**9 + 7)
                    
                elif int(s[i:idx]) > k:
                    break
            
            return ans
        
        return back_track(len(s)) % (10**9 + 7)