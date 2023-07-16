class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        @cache
        def back_track(idx):
            if idx == n:
                return 1
            
            if s[idx] == "0":
                return 0
            
            ans = back_track(idx+1)
            if idx + 2 <= n and int(s[idx:idx+2]) < 27:
                ans += back_track(idx+2)
                
            return ans
        
        return back_track(0)