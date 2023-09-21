class Solution:
    def checkPartitioning(self, s: str) -> bool:
        N = len(s)
        
        def IsPalindrome(arr):
            return arr == arr[::-1]
        
        @cache
        def dp(idx, count):
            if count == 2:
                return idx < N and IsPalindrome(s[idx:])
            
            for i in range(idx, N):
                curr = s[idx : i + 1]
                
                if IsPalindrome(curr) and dp(i + 1, count + 1):
                    return True
                
        return dp(0, 0)