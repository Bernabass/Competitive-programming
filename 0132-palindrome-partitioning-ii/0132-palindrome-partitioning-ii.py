class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        
        def IsPalindrome(arr):
            return arr == arr[::-1]
        
        @cache
        def dp(idx):
            if idx == N:
                return -1
            
            min_cut = inf
            for i in range(idx, N):
                curr = s[idx : i + 1]
                
                if IsPalindrome(curr):
                    min_cut = min(min_cut, 1 + dp(i + 1))
                    
            return min_cut
        
        return dp(0)